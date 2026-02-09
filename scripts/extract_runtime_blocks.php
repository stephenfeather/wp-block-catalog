<?php
// Extract registered block metadata from a live WordPress runtime.

$out_path = getenv('OUT_PATH') ?: null;

if (!class_exists('WP_Block_Type_Registry')) {
    fwrite(STDERR, "WP_Block_Type_Registry not available. Run via wp-cli with WordPress loaded.\n");
    exit(1);
}

$registry = WP_Block_Type_Registry::get_instance()->get_all_registered();
$blocks = [];

foreach ($registry as $block) {
    $blocks[] = [
        'name' => $block->name,
        'title' => $block->title,
        'category' => $block->category,
        'keywords' => $block->keywords,
        'apiVersion' => $block->api_version,
        'attributes' => $block->attributes,
        'supports' => $block->supports,
        'usesContext' => $block->uses_context,
        'providesContext' => $block->provides_context,
        'example' => $block->example,
        'isDynamic' => !empty($block->render_callback),
    ];
}

$payload = [
    'generated_at_utc' => gmdate('c'),
    'count' => count($blocks),
    'blocks' => $blocks,
];

$json = wp_json_encode($payload, JSON_PRETTY_PRINT);

if ($out_path) {
    file_put_contents($out_path, $json);
} else {
    echo $json;
}
