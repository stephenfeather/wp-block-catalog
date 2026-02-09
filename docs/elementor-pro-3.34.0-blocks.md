---
wordpress_version: 6.9.1
generated_at_utc: 2026-02-09T15:05:39Z
plugin_slug: elementor-pro
plugin_version: 3.34.0
---

# WordPress Blocks Catalog (WP 6.9.1, elementor-pro 3.34.0)

## core/gallery
**Title:** Gallery
**Category:** media
**API Version:** 3
**Origin:** plugin (elementor-pro)
**Dynamic:** true

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| allowResize | boolean | false |  |  |
| aspectRatio | string | auto |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| caption | rich-text |  | rich-text | .blocks-gallery-caption |
| className | string |  |  |  |
| columns | number |  |  |  |
| fixedHeight | boolean | true |  |  |
| gradient | string |  |  |  |
| ids | array | [] |  |  |
| imageCrop | boolean | true |  |  |
| images | array | [] | query | .blocks-gallery-item |
| layout | object |  |  |  |
| linkTarget | string |  |  |  |
| linkTo | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| randomOrder | boolean | false |  |  |
| shortCodeTransforms | array | [] |  |  |
| sizeSlug | string | large |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "color": true,
      "radius": true
    },
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": true,
  "anchor": true,
  "color": {
    "background": true,
    "gradients": true,
    "text": false
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
      "type": "flex"
    }
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true,
      "margin": false,
      "padding": false
    },
    "__experimentalSkipSerialization": [
      "blockGap"
    ],
    "blockGap": [
      "horizontal",
      "vertical"
    ],
    "margin": true,
    "padding": true
  },
  "units": [
    "px",
    "em",
    "rem",
    "vh",
    "vw"
  ]
}
```

### Example Markup
_Not generated yet._

---
## core/image
**Title:** Image
**Category:** media
**API Version:** 3
**Origin:** plugin (elementor-pro)
**Dynamic:** true

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alt | string |  | attribute | img | alt |
| aspectRatio | string |  |  |  |
| blob | string |  |  |  |
| borderColor | string |  |  |  |
| caption | rich-text |  | rich-text | figcaption |
| className | string |  |  |  |
| height | string |  |  |  |
| href | string |  | attribute | figure > a | href |
| id | number |  |  |  |
| lightbox | object |  |  |  |
| linkClass | string |  | attribute | figure > a | class |
| linkDestination | string |  |  |  |
| linkTarget | string |  | attribute | figure > a | target |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| rel | string |  | attribute | figure > a | rel |
| scale | string |  |  |  |
| sizeSlug | string |  |  |  |
| style | object |  |  |  |
| title | string |  | attribute | img | title |
| url | string |  | attribute | img | src |
| width | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "color": true,
      "radius": true,
      "width": true
    },
    "__experimentalSkipSerialization": true,
    "color": true,
    "radius": true,
    "width": true
  },
  "align": [
    "left",
    "center",
    "right",
    "wide",
    "full"
  ],
  "anchor": true,
  "color": {
    "background": false,
    "text": false
  },
  "filter": {
    "duotone": true
  },
  "interactivity": true,
  "shadow": {
    "__experimentalSkipSerialization": true
  },
  "spacing": {
    "margin": true
  }
}
```

### Example Markup
_Not generated yet._

---