---
wordpress_version: 6.9.1
generated_at_utc: 2026-02-09T15:05:39Z
plugin_slug: shoptimizer
plugin_version: 2.9.1
---

# WordPress Blocks Catalog (WP 6.9.1, shoptimizer 2.9.1)

## core/columns
**Title:** Columns
**Category:** design
**API Version:** 3
**Origin:** plugin (shoptimizer)
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| isStackedOnMobile | boolean | true |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| templateLock | ["string", "boolean"] |  |  |  |
| textColor | string |  |  |  |
| verticalAlignment | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "color": true,
      "radius": true,
      "style": true,
      "width": true
    },
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": [
    "wide",
    "full"
  ],
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "button": true,
    "gradients": true,
    "heading": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": {
    "allowEditing": false,
    "allowInheriting": false,
    "allowSwitching": false,
    "default": {
      "flexWrap": "nowrap",
      "type": "flex"
    }
  },
  "shadow": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true,
      "padding": true
    },
    "blockGap": {
      "__experimentalDefault": "2em",
      "sides": [
        "horizontal",
        "vertical"
      ]
    },
    "margin": [
      "top",
      "bottom"
    ],
    "padding": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": true
    },
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalTextDecoration": true,
    "__experimentalTextTransform": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/spacer
**Title:** Spacer
**Category:** design
**API Version:** 3
**Origin:** plugin (shoptimizer)
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| height | string | 100px |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| width | string |  |  |  |

### Supports
```json
{
  "anchor": true,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": true
    },
    "margin": [
      "top",
      "bottom"
    ]
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/classic-shortcode
**Title:** Classic Shortcode
**Category:** woocommerce
**API Version:** 3
**Origin:** plugin (shoptimizer)
**Dynamic:** true

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| shortcode | string | cart |  |  |

### Supports
```json
{
  "align": true,
  "html": false,
  "inserter": true,
  "interactivity": {
    "clientNavigation": false
  },
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---