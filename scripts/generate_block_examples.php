<?php
// Generate example Gutenberg block markup using a WordPress runtime.
// Usage: php generate_block_examples.php --wp-root=/path/to/wordpress --out=/path/to/examples.json

$options = getopt('', ['wp-root:', 'out:']);
if (!isset($options['wp-root']) || !isset($options['out'])) {
    fwrite(STDERR, "Usage: php generate_block_examples.php --wp-root=/path/to/wordpress --out=/path/to/examples.json\n");
    exit(1);
}

$wp_root = rtrim($options['wp-root'], '/');
$out_path = $options['out'];

$wp_load = $wp_root . '/wp-load.php';
if (!file_exists($wp_load)) {
    fwrite(STDERR, "Could not find wp-load.php at: {$wp_load}\n");
    exit(1);
}

define('WP_USE_THEMES', false);
require_once $wp_load;

if (!class_exists('WP_Block_Type_Registry')) {
    fwrite(STDERR, "WP_Block_Type_Registry not available. Ensure WordPress is loaded.\n");
    exit(1);
}

function build_block_from_example($block_name, $example) {
    $attrs = $example['attributes'] ?? [];
    $inner_blocks = [];
    $inner_content = [];

    if (!empty($example['innerBlocks']) && is_array($example['innerBlocks'])) {
        foreach ($example['innerBlocks'] as $inner) {
            $inner_name = $inner['blockName'] ?? $inner['name'] ?? null;
            if (!$inner_name) {
                continue;
            }
            $inner_example = [
                'attributes' => $inner['attrs'] ?? ($inner['attributes'] ?? []),
                'innerBlocks' => $inner['innerBlocks'] ?? [],
            ];
            $inner_blocks[] = build_block_from_example($inner_name, $inner_example);
            $inner_content[] = null;
        }
    }

    return [
        'blockName' => $block_name,
        'attrs' => $attrs,
        'innerBlocks' => $inner_blocks,
        'innerHTML' => $example['innerHTML'] ?? '',
        'innerContent' => $example['innerContent'] ?? $inner_content,
    ];
}

function build_simple_block($block_name, $attrs, $inner_html) {
    return [
        'blockName' => $block_name,
        'attrs' => $attrs,
        'innerBlocks' => [],
        'innerHTML' => $inner_html,
        'innerContent' => [$inner_html],
    ];
}

function build_container_block($block_name, $attrs, $inner_blocks) {
    $inner_content = [];
    foreach ($inner_blocks as $_) {
        $inner_content[] = null;
    }
    return [
        'blockName' => $block_name,
        'attrs' => $attrs,
        'innerBlocks' => $inner_blocks,
        'innerHTML' => '',
        'innerContent' => $inner_content,
    ];
}

function default_example_for($block_name) {
    switch ($block_name) {
        case 'core/paragraph':
            return build_simple_block($block_name, [], '<p>Example paragraph.</p>');
        case 'core/heading':
            return build_simple_block($block_name, ['level' => 2], '<h2>Example heading</h2>');
        case 'core/list':
            return build_simple_block($block_name, [], '<ul><li>Item one</li><li>Item two</li></ul>');
        case 'core/quote':
            return build_simple_block(
                $block_name,
                [],
                '<blockquote class="wp-block-quote"><p>Quote text.</p><cite>Author</cite></blockquote>'
            );
        case 'core/code':
            return build_simple_block(
                $block_name,
                [],
                '<pre class="wp-block-code"><code>const x = 1;</code></pre>'
            );
        case 'core/preformatted':
            return build_simple_block(
                $block_name,
                [],
                '<pre class="wp-block-preformatted">Preformatted text</pre>'
            );
        case 'core/table':
            return build_simple_block(
                $block_name,
                [],
                '<figure class="wp-block-table"><table><tbody><tr><td>A</td><td>B</td></tr></tbody></table></figure>'
            );
        case 'core/buttons':
            $button = build_simple_block(
                'core/button',
                [],
                '<div class="wp-block-button"><a class="wp-block-button__link">Click me</a></div>'
            );
            return build_container_block($block_name, [], [$button]);
        case 'core/group':
            $para = build_simple_block('core/paragraph', [], '<p>Grouped paragraph.</p>');
            return build_container_block($block_name, [], [$para]);
        case 'core/columns':
            $left = build_container_block('core/column', [], [
                build_simple_block('core/paragraph', [], '<p>Left column</p>'),
            ]);
            $right = build_container_block('core/column', [], [
                build_simple_block('core/paragraph', [], '<p>Right column</p>'),
            ]);
            return build_container_block($block_name, [], [$left, $right]);
        case 'core/cover':
            return build_simple_block(
                $block_name,
                ['overlayColor' => 'black', 'minHeight' => 200],
                '<div class="wp-block-cover" style="min-height:200px"><span class="wp-block-cover__background has-black-background-color"></span><div class="wp-block-cover__inner-container"><p>Cover content</p></div></div>'
            );
        case 'core/media-text':
            return build_simple_block(
                $block_name,
                ['mediaPosition' => 'left'],
                '<div class="wp-block-media-text"><figure class="wp-block-media-text__media"><img src="https://example.com/image.jpg" alt="Example image" /></figure><div class="wp-block-media-text__content"><p>Media text content</p></div></div>'
            );
        default:
            return null;
    }
}

function extract_attribute_defaults($block_type) {
    $defaults = [];
    if (!isset($block_type->attributes) || !is_array($block_type->attributes)) {
        return $defaults;
    }
    foreach ($block_type->attributes as $attr_name => $schema) {
        if (!is_array($schema)) {
            continue;
        }
        if (array_key_exists('default', $schema)) {
            $defaults[$attr_name] = $schema['default'];
        }
    }
    return $defaults;
}

function is_dynamic_block($block_type) {
    return !empty($block_type->render_callback);
}

$registry = WP_Block_Type_Registry::get_instance();
$blocks = $registry->get_all_registered();

$examples = [];

foreach ($blocks as $name => $block_type) {
    $example = $block_type->example ?? null;
    $block = null;

    $source = 'empty';
    if (is_array($example)) {
        $block = build_block_from_example($name, $example);
        $source = 'block-example';
    } else {
        $block = default_example_for($name);
        if ($block) {
            $source = 'default-example';
        } else {
            $defaults = extract_attribute_defaults($block_type);
            $block = [
                'blockName' => $name,
                'attrs' => $defaults,
                'innerBlocks' => [],
                'innerHTML' => '',
                'innerContent' => [],
            ];
            $source = is_dynamic_block($block_type) ? 'default-attrs' : 'empty';
        }
    }

    $markup = '';
    if (function_exists('serialize_block')) {
        $markup = serialize_block($block);
    } elseif (function_exists('serialize_blocks')) {
        $markup = serialize_blocks([$block]);
    }

    $examples[$name] = [
        'markup' => $markup,
        'variants' => [],
        'source' => $source,
        'attrDefaults' => extract_attribute_defaults($block_type),
        'isDynamic' => is_dynamic_block($block_type)
    ];
}

$payload = [
    'wordpressVersion' => get_bloginfo('version'),
    'generatedAtUtc' => gmdate('Y-m-d\TH:i:s\Z'),
    'examples' => $examples,
];

file_put_contents($out_path, json_encode($payload, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));

fwrite(STDOUT, "Wrote examples to {$out_path}\n");
