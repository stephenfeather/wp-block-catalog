---
wordpress_version: 6.9.1
generated_at_utc: 2026-02-09T15:01:00Z
source_roots: core: /Users/stephenfeather/Development/wp-block-catalog/artifacts/wp-6.9.1-src/wordpress/wp-includes/blocks
---

# WordPress Blocks Catalog (6.9.1)

## core/accordion
**Title:** Accordion
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| autoclose | boolean | false |  |  |
| headingLevel | number | 3 |  |  |
| iconPosition | string | right |  |  |
| levelOptions | array |  |  |  |
| showIcon | boolean | true |  |  |

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
  "ariaLabel": true,
  "background": {
    "__experimentalDefaultControls": {
      "backgroundImage": true
    },
    "backgroundImage": true,
    "backgroundSize": true
  },
  "color": {
    "background": true,
    "gradients": true
  },
  "contentRole": true,
  "html": false,
  "interactivity": true,
  "layout": true,
  "shadow": true,
  "spacing": {
    "blockGap": true,
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
## core/accordion-heading
**Title:** Accordion Heading
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| iconPosition | string | right |  |  |
| level | number |  |  |  |
| openByDefault | boolean | false |  |  |
| showIcon | boolean | true |  |  |
| title | rich-text |  | rich-text | .wp-block-accordion-heading__toggle-title |

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
  "align": false,
  "anchor": true,
  "color": {
    "background": true,
    "gradients": true
  },
  "interactivity": true,
  "lock": false,
  "shadow": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "padding": true
    },
    "__experimentalSelector": ".wp-block-accordion-heading__toggle",
    "__experimentalSkipSerialization": true,
    "padding": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontFamily": true,
      "fontSize": true
    },
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalSkipSerialization": [
      "textDecoration",
      "letterSpacing"
    ],
    "__experimentalTextDecoration": true,
    "__experimentalTextTransform": true,
    "fontSize": true
  },
  "visibility": false
}
```

### Example Markup
_Not generated yet._

---
## core/accordion-item
**Title:** Accordion Item
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| openByDefault | boolean | false |  |  |

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
  "color": {
    "background": true,
    "gradients": true
  },
  "contentRole": true,
  "html": false,
  "interactivity": true,
  "layout": {
    "allowEditing": false
  },
  "shadow": true,
  "spacing": {
    "blockGap": true,
    "margin": [
      "top",
      "bottom"
    ]
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
## core/accordion-panel
**Title:** Accordion Panel
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isSelected | boolean | false |  |  |
| openByDefault | boolean | false |  |  |
| templateLock | ["string", "boolean"] | false |  |  |

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
  "allowedBlocks": true,
  "color": {
    "background": true,
    "gradients": true
  },
  "contentRole": true,
  "html": false,
  "interactivity": true,
  "layout": {
    "allowEditing": false
  },
  "lock": false,
  "shadow": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true,
      "padding": true
    },
    "blockGap": true,
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
  },
  "visibility": false
}
```

### Example Markup
_Not generated yet._

---
## core/archives
**Title:** Archives
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| displayAsDropdown | boolean | false |  |  |
| showLabel | boolean | true |  |  |
| showPostCounts | boolean | false |  |  |
| type | string | monthly |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
## core/audio
**Title:** Audio
**Category:** media
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| autoplay | boolean |  | attribute | audio | autoplay |
| blob | string |  |  |  |
| caption | rich-text |  | rich-text | figcaption |
| id | number |  |  |  |
| loop | boolean |  | attribute | audio | loop |
| preload | string |  | attribute | audio | preload |
| src | string |  | attribute | audio | src |

### Supports
```json
{
  "align": true,
  "anchor": true,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/avatar
**Title:** Avatar
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isLink | boolean | false |  |  |
| linkTarget | string | _self |  |  |
| size | number | 96 |  |  |
| userId | number |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "radius": true
    },
    "__experimentalSkipSerialization": true,
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": true,
  "alignWide": false,
  "color": {
    "background": false,
    "text": false
  },
  "filter": {
    "duotone": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/block
**Title:** Pattern
**Category:** reusable
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | object | {} |  |  |
| ref | number |  |  |  |

### Supports
```json
{
  "customClassName": false,
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "renaming": false
}
```

### Example Markup
_Not generated yet._

---
## core/button
**Title:** Button
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| gradient | string |  |  |  |
| linkTarget | string |  | attribute | a | target |
| placeholder | string |  |  |  |
| rel | string |  | attribute | a | rel |
| tagName | string | a |  |  |
| text | rich-text |  | rich-text | a,button |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |
| title | string |  | attribute | a,button | title |
| type | string | button |  |  |
| url | string |  | attribute | a | href |
| width | number |  |  |  |

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
    "__experimentalSkipSerialization": true,
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": false,
  "alignWide": false,
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "__experimentalSkipSerialization": true,
    "gradients": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
  "shadow": {
    "__experimentalSkipSerialization": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "padding": true
    },
    "__experimentalSkipSerialization": true,
    "padding": [
      "horizontal",
      "vertical"
    ]
  },
  "splitting": true,
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": true
    },
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalSkipSerialization": [
      "fontSize",
      "lineHeight",
      "fontFamily",
      "fontWeight",
      "fontStyle",
      "textTransform",
      "textDecoration",
      "letterSpacing"
    ],
    "__experimentalTextDecoration": true,
    "__experimentalTextTransform": true,
    "__experimentalWritingMode": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/buttons
**Title:** Buttons
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
_None_

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
  "__experimentalExposeControlsToChildren": true,
  "align": [
    "wide",
    "full"
  ],
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true
    },
    "gradients": true,
    "text": false
  },
  "contentRole": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": {
    "allowInheriting": false,
    "allowSwitching": false,
    "default": {
      "type": "flex"
    }
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true
    },
    "blockGap": [
      "horizontal",
      "vertical"
    ],
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
## core/calendar
**Title:** Calendar
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| month | integer |  |  |  |
| year | integer |  |  |  |

### Supports
```json
{
  "align": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "__experimentalSelector": "table, th",
    "__experimentalSkipSerialization": [
      "text",
      "background"
    ],
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": true
    },
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalTextTransform": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/categories
**Title:** Terms List
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| displayAsDropdown | boolean | false |  |  |
| label | string |  |  |  |
| showEmpty | boolean | false |  |  |
| showHierarchy | boolean | false |  |  |
| showLabel | boolean | true |  |  |
| showOnlyTopLevel | boolean | false |  |  |
| showPostCounts | boolean | false |  |  |
| taxonomy | string | category |  |  |

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
  "align": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
## core/code
**Title:** Code
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | rich-text |  | rich-text | code |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "color": true,
      "width": true
    },
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": [
    "wide"
  ],
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "background": true,
    "gradients": true,
    "text": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
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
## core/column
**Title:** Column
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| templateLock | ["string", "boolean"] |  |  |  |
| verticalAlignment | string |  |  |  |
| width | string |  |  |  |

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
  "__experimentalOnEnter": true,
  "allowedBlocks": true,
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
  "layout": true,
  "reusable": false,
  "shadow": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true,
      "padding": true
    },
    "blockGap": true,
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
## core/columns
**Title:** Columns
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isStackedOnMobile | boolean | true |  |  |
| templateLock | ["string", "boolean"] |  |  |  |
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
## core/comment-author-name
**Title:** Comment Author Name
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isLink | boolean | true |  |  |
| linkTarget | string | _self |  |  |
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/comment-content
**Title:** Comment Content
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "spacing": {
    "__experimentalDefaultControls": {
      "padding": true
    },
    "padding": [
      "horizontal",
      "vertical"
    ]
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
## core/comment-date
**Title:** Comment Date
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| format | string |  |  |  |
| isLink | boolean | true |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/comment-edit-link
**Title:** Comment Edit Link
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| linkTarget | string | _self |  |  |
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true
    },
    "gradients": true,
    "link": true,
    "text": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
## core/comment-reply-link
**Title:** Comment Reply Link
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true
    },
    "gradients": true,
    "link": true,
    "text": false
  },
  "html": false,
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
## core/comment-template
**Title:** Comment Template
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
_None_

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
  "align": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
  "spacing": {
    "margin": true,
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
## core/comments
**Title:** Comments
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| legacy | boolean | false |  |  |
| tagName | string | div |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "heading": true,
    "link": true
  },
  "html": false,
  "spacing": {
    "margin": true,
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
## core/comments-pagination
**Title:** Comments Pagination
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| paginationArrow | string | none |  |  |

### Supports
```json
{
  "align": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": {
    "allowInheriting": false,
    "allowSwitching": false,
    "default": {
      "type": "flex"
    }
  },
  "reusable": false,
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
## core/comments-pagination-next
**Title:** Comments Next Page
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

### Supports
```json
{
  "color": {
    "__experimentalDefaultControls": {
      "background": true
    },
    "gradients": true,
    "text": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
## core/comments-pagination-numbers
**Title:** Comments Page Numbers
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "color": {
    "__experimentalDefaultControls": {
      "background": true
    },
    "gradients": true,
    "text": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
## core/comments-pagination-previous
**Title:** Comments Previous Page
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

### Supports
```json
{
  "color": {
    "__experimentalDefaultControls": {
      "background": true
    },
    "gradients": true,
    "text": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
## core/comments-title
**Title:** Comments Title
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| level | number | 2 |  |  |
| levelOptions | array |  |  |  |
| showCommentsCount | boolean | true |  |  |
| showPostTitle | boolean | true |  |  |
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": true,
  "anchor": false,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "__experimentalFontFamily": true,
      "__experimentalFontStyle": true,
      "__experimentalFontWeight": true,
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
## core/cover
**Title:** Cover
**Category:** media
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alt | string |  |  |  |
| backgroundType | string | image |  |  |
| contentPosition | string |  |  |  |
| customGradient | string |  |  |  |
| customOverlayColor | string |  |  |  |
| dimRatio | number | 100 |  |  |
| focalPoint | object |  |  |  |
| gradient | string |  |  |  |
| hasParallax | boolean | false |  |  |
| id | number |  |  |  |
| isDark | boolean | true |  |  |
| isRepeated | boolean | false |  |  |
| isUserOverlayColor | boolean |  |  |  |
| minHeight | number |  |  |  |
| minHeightUnit | string |  |  |  |
| overlayColor | string |  |  |  |
| poster | string |  | attribute | video | poster |
| sizeSlug | string |  |  |  |
| tagName | string | div |  |  |
| templateLock | ["string", "boolean"] |  |  |  |
| url | string |  |  |  |
| useFeaturedImage | boolean | false |  |  |

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
  "align": true,
  "allowedBlocks": true,
  "anchor": true,
  "color": {
    "__experimentalSkipSerialization": [
      "gradients"
    ],
    "background": false,
    "enableContrastChecker": false,
    "heading": true,
    "text": true
  },
  "dimensions": {
    "aspectRatio": true
  },
  "filter": {
    "duotone": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": {
    "allowJustification": false
  },
  "shadow": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true,
      "padding": true
    },
    "blockGap": true,
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
## core/details
**Title:** Details
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  | attribute | .wp-block-details | name |
| placeholder | string |  |  |  |
| showContent | boolean | false |  |  |
| summary | rich-text |  | rich-text | summary |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "style": true,
    "width": true
  },
  "__experimentalOnEnter": true,
  "align": [
    "wide",
    "full"
  ],
  "allowedBlocks": true,
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": {
    "allowEditing": false
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "blockGap": true,
    "margin": true,
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
## core/embed
**Title:** Embed
**Category:** embed
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| allowResponsive | boolean | true |  |  |
| caption | rich-text |  | rich-text | figcaption |
| previewable | boolean | true |  |  |
| providerNameSlug | string |  |  |  |
| responsive | boolean | false |  |  |
| type | string |  |  |  |
| url | string |  |  |  |

### Supports
```json
{
  "align": true,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/file
**Title:** File
**Category:** media
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| blob | string |  |  |  |
| displayPreview | boolean |  |  |  |
| downloadButtonText | rich-text |  | rich-text | a[download] |
| fileId | string |  | attribute | a:not([download]) | id |
| fileName | rich-text |  | rich-text | a:not([download]) |
| href | string |  |  |  |
| id | number |  |  |  |
| previewHeight | number | 600 |  |  |
| showDownloadButton | boolean | true |  |  |
| textLinkHref | string |  | attribute | a:not([download]) | href |
| textLinkTarget | string |  | attribute | a:not([download]) | target |

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
  "align": true,
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true
    },
    "gradients": true,
    "link": true,
    "text": false
  },
  "interactivity": true,
  "spacing": {
    "margin": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/footnotes
**Title:** Footnotes
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "color": false,
      "radius": false,
      "style": false,
      "width": false
    },
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "link": true,
      "text": true
    },
    "background": true,
    "link": true,
    "text": true
  },
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "multiple": false,
  "reusable": false,
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
    "__experimentalWritingMode": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/freeform
**Title:** Classic
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  | raw |  |

### Supports
```json
{
  "className": false,
  "customClassName": false,
  "lock": false,
  "renaming": false,
  "reusable": false,
  "visibility": false
}
```

### Example Markup
_Not generated yet._

---
## core/gallery
**Title:** Gallery
**Category:** media
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| allowResize | boolean | false |  |  |
| aspectRatio | string | auto |  |  |
| caption | rich-text |  | rich-text | .blocks-gallery-caption |
| columns | number |  |  |  |
| fixedHeight | boolean | true |  |  |
| ids | array | [] |  |  |
| imageCrop | boolean | true |  |  |
| images | array | [] | query | .blocks-gallery-item |
| linkTarget | string |  |  |  |
| linkTo | string |  |  |  |
| randomOrder | boolean | false |  |  |
| shortCodeTransforms | array | [] |  |  |
| sizeSlug | string | large |  |  |

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
## core/group
**Title:** Group
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| tagName | string | div |  |  |
| templateLock | ["string", "boolean"] |  |  |  |

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
  "__experimentalOnEnter": true,
  "__experimentalOnMerge": true,
  "__experimentalSettings": true,
  "align": [
    "wide",
    "full"
  ],
  "allowedBlocks": true,
  "anchor": true,
  "ariaLabel": true,
  "background": {
    "__experimentalDefaultControls": {
      "backgroundImage": true
    },
    "backgroundImage": true,
    "backgroundSize": true
  },
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
  "dimensions": {
    "minHeight": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": {
    "allowSizingOnChildren": true
  },
  "position": {
    "sticky": true
  },
  "shadow": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true,
      "padding": true
    },
    "blockGap": true,
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
## core/heading
**Title:** Heading
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | rich-text |  | rich-text | h1,h2,h3,h4,h5,h6 |
| level | number | 2 |  |  |
| levelOptions | array |  |  |  |
| placeholder | string |  |  |  |
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "__experimentalSlashInserter": true,
  "__unstablePasteTextInline": true,
  "align": [
    "wide",
    "full"
  ],
  "anchor": true,
  "className": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
    "padding": true
  },
  "splitting": true,
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
    "__experimentalWritingMode": true,
    "fitText": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/home-link
**Title:** Home Link
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

### Supports
```json
{
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
## core/html
**Title:** Custom HTML
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  | raw |  |

### Supports
```json
{
  "className": false,
  "customClassName": false,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/image
**Title:** Image
**Category:** media
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alt | string |  | attribute | img | alt |
| aspectRatio | string |  |  |  |
| blob | string |  |  |  |
| caption | rich-text |  | rich-text | figcaption |
| height | string |  |  |  |
| href | string |  | attribute | figure > a | href |
| id | number |  |  |  |
| lightbox | object |  |  |  |
| linkClass | string |  | attribute | figure > a | class |
| linkDestination | string |  |  |  |
| linkTarget | string |  | attribute | figure > a | target |
| rel | string |  | attribute | figure > a | rel |
| scale | string |  |  |  |
| sizeSlug | string |  |  |  |
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
## core/latest-comments
**Title:** Latest Comments
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| commentsToShow | number | 5 |  |  |
| displayAvatar | boolean | true |  |  |
| displayDate | boolean | true |  |  |
| displayExcerpt | boolean | true |  |  |

### Supports
```json
{
  "align": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/latest-posts
**Title:** Latest Posts
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| addLinkToFeaturedImage | boolean | false |  |  |
| categories | array |  |  |  |
| columns | number | 3 |  |  |
| displayAuthor | boolean | false |  |  |
| displayFeaturedImage | boolean | false |  |  |
| displayPostContent | boolean | false |  |  |
| displayPostContentRadio | string | excerpt |  |  |
| displayPostDate | boolean | false |  |  |
| excerptLength | number | 55 |  |  |
| featuredImageAlign | string |  |  |  |
| featuredImageSizeHeight | number |  |  |  |
| featuredImageSizeSlug | string | thumbnail |  |  |
| featuredImageSizeWidth | number |  |  |  |
| order | string | desc |  |  |
| orderBy | string | date |  |  |
| postLayout | string | list |  |  |
| postsToShow | number | 5 |  |  |
| selectedAuthor | number |  |  |  |

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
  "align": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/legacy-widget
**Title:** Legacy Widget
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| id | string |  |  |  |
| idBase | string |  |  |  |
| instance | object |  |  |  |

### Supports
```json
{
  "customClassName": false,
  "html": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## core/list
**Title:** List
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| ordered | boolean | false |  |  |
| placeholder | string |  |  |  |
| reversed | boolean |  |  |  |
| start | number |  |  |  |
| type | string |  |  |  |
| values | string |  | html | ol,ul |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "__experimentalOnMerge": true,
  "__experimentalSlashInserter": true,
  "__unstablePasteTextInline": true,
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
## core/list-item
**Title:** List Item
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | rich-text |  | rich-text | li |
| placeholder | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "anchor": true,
  "className": false,
  "color": {
    "__experimentalDefaultControls": {
      "text": true
    },
    "background": true,
    "gradients": true,
    "link": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
    "padding": true
  },
  "splitting": true,
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
## core/loginout
**Title:** Login/out
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| displayLoginAsForm | boolean | false |  |  |
| redirectToCurrent | boolean | true |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "className": true,
  "color": {
    "background": true,
    "gradients": true,
    "link": true,
    "text": false
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
## core/math
**Title:** Math
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| latex | string |  |  |  |
| mathML | string |  | html | math |

### Supports
```json
{
  "html": false
}
```

### Example Markup
_Not generated yet._

---
## core/media-text
**Title:** Media & Text
**Category:** media
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | none |  |  |
| focalPoint | object |  |  |  |
| href | string |  | attribute | figure a | href |
| imageFill | boolean |  |  |  |
| isStackedOnMobile | boolean | true |  |  |
| linkClass | string |  | attribute | figure a | class |
| linkDestination | string |  |  |  |
| linkTarget | string |  | attribute | figure a | target |
| mediaAlt | string |  | attribute | figure img | alt |
| mediaId | number |  |  |  |
| mediaLink | string |  |  |  |
| mediaPosition | string | left |  |  |
| mediaSizeSlug | string |  |  |  |
| mediaType | string |  |  |  |
| mediaUrl | string |  | attribute | figure video,figure img | src |
| mediaWidth | number | 50 |  |  |
| rel | string |  | attribute | figure a | rel |
| useFeaturedImage | boolean | false |  |  |
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
  "allowedBlocks": true,
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "heading": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/missing
**Title:** Unsupported
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| originalContent | string |  | raw |  |
| originalName | string |  |  |  |
| originalUndelimitedContent | string |  |  |  |

### Supports
```json
{
  "className": false,
  "customClassName": false,
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "lock": false,
  "renaming": false,
  "reusable": false,
  "visibility": false
}
```

### Example Markup
_Not generated yet._

---
## core/more
**Title:** More
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| customText | string |  |  |  |
| noTeaser | boolean | false |  |  |

### Supports
```json
{
  "className": false,
  "customClassName": false,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## core/navigation
**Title:** Navigation
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| __unstableLocation | string |  |  |  |
| backgroundColor | string |  |  |  |
| customBackgroundColor | string |  |  |  |
| customOverlayBackgroundColor | string |  |  |  |
| customOverlayTextColor | string |  |  |  |
| customTextColor | string |  |  |  |
| hasIcon | boolean | true |  |  |
| icon | string | handle |  |  |
| maxNestingLevel | number | 5 |  |  |
| openSubmenusOnClick | boolean | false |  |  |
| overlayBackgroundColor | string |  |  |  |
| overlayMenu | string | mobile |  |  |
| overlayTextColor | string |  |  |  |
| ref | number |  |  |  |
| rgbBackgroundColor | string |  |  |  |
| rgbTextColor | string |  |  |  |
| showSubmenuIcon | boolean | true |  |  |
| templateLock | ["string", "boolean"] |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "ariaLabel": true,
  "contentRole": true,
  "html": false,
  "inserter": true,
  "interactivity": true,
  "layout": {
    "allowInheriting": false,
    "allowSizingOnChildren": true,
    "allowSwitching": false,
    "allowVerticalAlignment": false,
    "default": {
      "type": "flex"
    }
  },
  "renaming": false,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true
    },
    "blockGap": true,
    "units": [
      "px",
      "em",
      "rem",
      "vh",
      "vw"
    ]
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": true
    },
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalSkipSerialization": [
      "textDecoration"
    ],
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
## core/navigation-link
**Title:** Custom Link
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| description | string |  |  |  |
| id | number |  |  |  |
| isTopLevelLink | boolean |  |  |  |
| kind | string |  |  |  |
| label | string |  |  |  |
| opensInNewTab | boolean | false |  |  |
| rel | string |  |  |  |
| title | string |  |  |  |
| type | string |  |  |  |
| url | string |  |  |  |

### Supports
```json
{
  "__experimentalSlashInserter": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "renaming": false,
  "reusable": false,
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
## core/navigation-submenu
**Title:** Submenu
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| description | string |  |  |  |
| id | number |  |  |  |
| isTopLevelItem | boolean |  |  |  |
| kind | string |  |  |  |
| label | string |  |  |  |
| opensInNewTab | boolean | false |  |  |
| rel | string |  |  |  |
| title | string |  |  |  |
| type | string |  |  |  |
| url | string |  |  |  |

### Supports
```json
{
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
## core/nextpage
**Title:** Page Break
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "className": false,
  "customClassName": false,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/page-list
**Title:** Page List
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isNested | boolean | false |  |  |
| parentPageID | integer | 0 |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "background": true,
    "gradients": true,
    "link": true,
    "text": true
  },
  "contentRole": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
## core/page-list-item
**Title:** Page List Item
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| hasChildren | boolean |  |  |  |
| id | number |  |  |  |
| label | string |  |  |  |
| link | string |  |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "lock": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## core/paragraph
**Title:** Paragraph
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| content | rich-text |  | rich-text | p |
| direction | string |  |  |  |
| dropCap | boolean | false |  |  |
| placeholder | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "__experimentalSelector": "p",
  "__unstablePasteTextInline": true,
  "anchor": true,
  "className": false,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
    "padding": true
  },
  "splitting": true,
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
    "__experimentalWritingMode": true,
    "fitText": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/pattern
**Title:** Pattern Placeholder
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| slug | string |  |  |  |

### Supports
```json
{
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "renaming": false,
  "visibility": false
}
```

### Example Markup
_Not generated yet._

---
## core/post-author
**Title:** Author
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| avatarSize | number | 48 |  |  |
| byline | string |  |  |  |
| isLink | boolean | false |  |  |
| linkTarget | string | _self |  |  |
| showAvatar | boolean | true |  |  |
| showBio | boolean |  |  |  |
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "filter": {
    "duotone": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/post-author-biography
**Title:** Author Biography
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/post-author-name
**Title:** Author Name
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isLink | boolean | false |  |  |
| linkTarget | string | _self |  |  |
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/post-comments-count
**Title:** Comments Count
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/post-comments-form
**Title:** Comments Form
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "heading": true,
    "link": true
  },
  "html": false,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": true
    },
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalTextTransform": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/post-comments-link
**Title:** Comments Link
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true
    },
    "link": true,
    "text": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/post-content
**Title:** Content
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| tagName | string | div |  |  |

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
  "background": {
    "__experimentalDefaultControls": {
      "backgroundImage": true
    },
    "backgroundImage": true,
    "backgroundSize": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": false,
      "text": false
    },
    "gradients": true,
    "heading": true,
    "link": true
  },
  "dimensions": {
    "minHeight": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "blockGap": true,
    "margin": true,
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
## core/post-date
**Title:** Date
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| datetime | string |  |  |  |
| format | string |  |  |  |
| isLink | boolean | false |  |  |
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/post-excerpt
**Title:** Excerpt
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| excerptLength | number | 55 |  |  |
| moreText | string |  |  |  |
| showMoreOnNewLine | boolean | true |  |  |
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/post-featured-image
**Title:** Featured Image
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| aspectRatio | string |  |  |  |
| customGradient | string |  |  |  |
| customOverlayColor | string |  |  |  |
| dimRatio | number | 0 |  |  |
| gradient | string |  |  |  |
| height | string |  |  |  |
| isLink | boolean | false |  |  |
| linkTarget | string | _self |  |  |
| overlayColor | string |  |  |  |
| rel | string |  |  | rel |
| scale | string | cover |  |  |
| sizeSlug | string |  |  |  |
| useFirstImageFromPost | boolean | false |  |  |
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
    "right",
    "center",
    "wide",
    "full"
  ],
  "color": {
    "background": false,
    "text": false
  },
  "filter": {
    "duotone": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "shadow": {
    "__experimentalSkipSerialization": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/post-navigation-link
**Title:** Post Navigation Link
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| arrow | string | none |  |  |
| label | string |  |  |  |
| linkLabel | boolean | false |  |  |
| showTitle | boolean | false |  |  |
| taxonomy | string |  |  |  |
| textAlign | string |  |  |  |
| type | string | next |  |  |

### Supports
```json
{
  "color": {
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
    "__experimentalWritingMode": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/post-template
**Title:** Post Template
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": true,
  "reusable": false,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true,
      "margin": false,
      "padding": false
    },
    "blockGap": {
      "__experimentalDefault": "1.25em"
    },
    "margin": true,
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
## core/post-terms
**Title:** Post Terms
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| prefix | string |  |  |  |
| separator | string | ,  |  |  |
| suffix | string |  |  |  |
| term | string |  |  |  |
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/post-time-to-read
**Title:** Time to Read
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| averageReadingSpeed | number | 189 |  |  |
| displayAsRange | boolean | true |  |  |
| displayMode | string | time |  |  |
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
## core/post-title
**Title:** Title
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isLink | boolean | false |  |  |
| level | number | 2 |  |  |
| levelOptions | array |  |  |  |
| linkTarget | string | _self |  |  |
| rel | string |  |  | rel |
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/preformatted
**Title:** Preformatted
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | rich-text |  | rich-text | pre |

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
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/pullquote
**Title:** Pullquote
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| citation | rich-text |  | rich-text | cite |
| textAlign | string |  |  |  |
| value | rich-text |  | rich-text | p |

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
  "__experimentalStyle": {
    "typography": {
      "fontSize": "1.5em",
      "lineHeight": "1.6"
    }
  },
  "align": [
    "left",
    "right",
    "wide",
    "full"
  ],
  "anchor": true,
  "background": {
    "__experimentalDefaultControls": {
      "backgroundImage": true
    },
    "backgroundImage": true,
    "backgroundSize": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "background": true,
    "gradients": true,
    "link": true
  },
  "dimensions": {
    "__experimentalDefaultControls": {
      "minHeight": false
    },
    "minHeight": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/query
**Title:** Query Loop
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| enhancedPagination | boolean | false |  |  |
| namespace | string |  |  |  |
| query | object | {"author": "", "exclude": [], "format": [], "inherit": true, "offset": 0, "order": "desc", "orderBy": "date", "pages": 0, "parents": [], "perPage": null, "postType": "post", "search": "", "sticky": "", "taxQuery": null} |  |  |
| queryId | number |  |  |  |
| tagName | string | div |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "contentRole": true,
  "html": false,
  "interactivity": true,
  "layout": true
}
```

### Example Markup
_Not generated yet._

---
## core/query-no-results
**Title:** No Results
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "align": true,
  "color": {
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
## core/query-pagination
**Title:** Pagination
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| paginationArrow | string | none |  |  |
| showLabel | boolean | true |  |  |

### Supports
```json
{
  "align": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": {
    "allowInheriting": false,
    "allowSwitching": false,
    "default": {
      "type": "flex"
    }
  },
  "reusable": false,
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
## core/query-pagination-next
**Title:** Next Page
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

### Supports
```json
{
  "color": {
    "__experimentalDefaultControls": {
      "background": true
    },
    "gradients": true,
    "text": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
## core/query-pagination-numbers
**Title:** Page Numbers
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| midSize | number | 2 |  |  |

### Supports
```json
{
  "color": {
    "__experimentalDefaultControls": {
      "background": true
    },
    "gradients": true,
    "text": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
## core/query-pagination-previous
**Title:** Previous Page
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

### Supports
```json
{
  "color": {
    "__experimentalDefaultControls": {
      "background": true
    },
    "gradients": true,
    "text": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false,
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
## core/query-title
**Title:** Query Title
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| level | number | 1 |  |  |
| levelOptions | array |  |  |  |
| showPrefix | boolean | true |  |  |
| showSearchTerm | boolean | true |  |  |
| textAlign | string |  |  |  |
| type | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/query-total
**Title:** Query Total
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| displayType | string | total-results |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/quote
**Title:** Quote
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| citation | rich-text |  | rich-text | cite |
| textAlign | string |  |  |  |
| value | string |  | html | blockquote |

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
  "__experimentalOnEnter": true,
  "__experimentalOnMerge": true,
  "align": [
    "left",
    "right",
    "wide",
    "full"
  ],
  "allowedBlocks": true,
  "anchor": true,
  "background": {
    "__experimentalDefaultControls": {
      "backgroundImage": true
    },
    "backgroundImage": true,
    "backgroundSize": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "heading": true,
    "link": true
  },
  "dimensions": {
    "__experimentalDefaultControls": {
      "minHeight": false
    },
    "minHeight": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": {
    "allowEditing": false
  },
  "spacing": {
    "blockGap": true,
    "margin": true,
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
## core/read-more
**Title:** Read More
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  |  |  |
| linkTarget | string | _self |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "width": true
    },
    "color": true,
    "radius": true,
    "width": true
  },
  "color": {
    "gradients": true,
    "text": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "padding": true
    },
    "margin": [
      "top",
      "bottom"
    ],
    "padding": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": true,
      "textDecoration": true
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
## core/rss
**Title:** RSS
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| blockLayout | string | list |  |  |
| columns | number | 2 |  |  |
| displayAuthor | boolean | false |  |  |
| displayDate | boolean | false |  |  |
| displayExcerpt | boolean | false |  |  |
| excerptLength | number | 55 |  |  |
| feedURL | string |  |  |  |
| itemsToShow | number | 5 |  |  |
| openInNewTab | boolean | false |  |  |
| rel | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": true,
  "color": {
    "background": true,
    "gradients": true,
    "link": true,
    "text": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/search
**Title:** Search
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| buttonPosition | string | button-outside |  |  |
| buttonText | string |  |  |  |
| buttonUseIcon | boolean | false |  |  |
| isSearchFieldHidden | boolean | false |  |  |
| label | string |  |  |  |
| placeholder | string |  |  |  |
| query | object | {} |  |  |
| showLabel | boolean | true |  |  |
| width | number |  |  |  |
| widthUnit | string |  |  |  |

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
    "right"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "__experimentalSkipSerialization": true,
    "gradients": true
  },
  "html": false,
  "interactivity": true,
  "spacing": {
    "margin": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": true
    },
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalSelector": ".wp-block-search__label, .wp-block-search__input, .wp-block-search__button",
    "__experimentalSkipSerialization": true,
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
## core/separator
**Title:** Separator
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| opacity | string | alpha-channel |  |  |
| tagName | string | hr |  |  |

### Supports
```json
{
  "align": [
    "center",
    "wide",
    "full"
  ],
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true
    },
    "__experimentalSkipSerialization": true,
    "background": true,
    "enableContrastChecker": false,
    "gradients": true,
    "text": false
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
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
## core/shortcode
**Title:** Shortcode
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| text | string |  | raw |  |

### Supports
```json
{
  "className": false,
  "customClassName": false,
  "html": false
}
```

### Example Markup
_Not generated yet._

---
## core/site-logo
**Title:** Site Logo
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isLink | boolean | true |  |  |
| linkTarget | string | _self |  |  |
| shouldSyncIcon | boolean |  |  |  |
| width | number |  |  |  |

### Supports
```json
{
  "align": true,
  "alignWide": false,
  "color": {
    "background": false,
    "text": false
  },
  "filter": {
    "duotone": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/site-tagline
**Title:** Site Tagline
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| level | number | 0 |  |  |
| levelOptions | array | [0, 1, 2, 3, 4, 5, 6] |  |  |
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true
  },
  "contentRole": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
    "__experimentalWritingMode": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/site-title
**Title:** Site Title
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isLink | boolean | true |  |  |
| level | number | 1 |  |  |
| levelOptions | array | [0, 1, 2, 3, 4, 5, 6] |  |  |
| linkTarget | string | _self |  |  |
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
    "__experimentalWritingMode": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/social-link
**Title:** Social Icon
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |
| rel | string |  |  |  |
| service | string |  |  |  |
| url | string |  |  |  |

### Supports
```json
{
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## core/social-links
**Title:** Social Icons
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| customIconBackgroundColor | string |  |  |  |
| customIconColor | string |  |  |  |
| iconBackgroundColor | string |  |  |  |
| iconBackgroundColorValue | string |  |  |  |
| iconColor | string |  |  |  |
| iconColorValue | string |  |  |  |
| openInNewTab | boolean | false |  |  |
| showLabels | boolean | false |  |  |
| size | string |  |  |  |

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
  "__experimentalExposeControlsToChildren": true,
  "align": [
    "left",
    "center",
    "right"
  ],
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": false
    },
    "background": true,
    "enableContrastChecker": false,
    "gradients": true,
    "text": false
  },
  "contentRole": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": {
    "allowInheriting": false,
    "allowSwitching": false,
    "allowVerticalAlignment": false,
    "default": {
      "type": "flex"
    }
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true,
      "margin": true,
      "padding": false
    },
    "blockGap": [
      "horizontal",
      "vertical"
    ],
    "margin": true,
    "padding": true,
    "units": [
      "px",
      "em",
      "rem",
      "vh",
      "vw"
    ]
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
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| height | string | 100px |  |  |
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
## core/table
**Title:** Table
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| body | array | [] | query | tbody tr |
| caption | rich-text |  | rich-text | figcaption |
| foot | array | [] | query | tfoot tr |
| hasFixedLayout | boolean | true |  |  |
| head | array | [] | query | thead tr |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "color": true,
      "style": true,
      "width": true
    },
    "__experimentalSkipSerialization": true,
    "color": true,
    "style": true,
    "width": true
  },
  "align": true,
  "anchor": true,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "__experimentalSkipSerialization": true,
    "gradients": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
## core/tag-cloud
**Title:** Tag Cloud
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| largestFontSize | string | 22pt |  |  |
| numberOfTags | number | 45 |  |  |
| showTagCounts | boolean | false |  |  |
| smallestFontSize | string | 8pt |  |  |
| taxonomy | string | post_tag |  |  |

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
  "align": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalTextTransform": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/template-part
**Title:** Template Part
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| area | string |  |  |  |
| slug | string |  |  |  |
| tagName | string |  |  |  |
| theme | string |  |  |  |

### Supports
```json
{
  "align": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "renaming": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## core/term-count
**Title:** Term Count
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| bracketType | string | round |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "color": true,
      "style": true,
      "width": true
    },
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
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
## core/term-description
**Title:** Term Description
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
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
## core/term-name
**Title:** Term Name
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isLink | boolean | false |  |  |
| level | number | 0 |  |  |
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalDefaultControls": {
      "color": true,
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
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "link": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
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
## core/term-template
**Title:** Term Template
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "layout": true,
  "reusable": false,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": true,
      "margin": false,
      "padding": false
    },
    "blockGap": {
      "__experimentalDefault": "1.25em"
    },
    "margin": true,
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
## core/terms-query
**Title:** Terms Query
**Category:** theme
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| tagName | string | div |  |  |
| termQuery | object | {"hideEmpty": true, "include": [], "inherit": false, "order": "asc", "orderBy": "name", "perPage": 10, "showNested": false, "taxonomy": "category"} |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "interactivity": true,
  "layout": true
}
```

### Example Markup
_Not generated yet._

---
## core/text-columns
**Title:** Text Columns (deprecated)
**Category:** design
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| columns | number | 2 |  |  |
| content | array | [{}, {}] | query | p |
| width | string |  |  |  |

### Supports
```json
{
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/verse
**Title:** Verse
**Category:** text
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | rich-text |  | rich-text | pre |
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "radius": true,
    "style": true,
    "width": true
  },
  "anchor": true,
  "background": {
    "__experimentalDefaultControls": {
      "backgroundImage": true
    },
    "backgroundImage": true,
    "backgroundSize": true
  },
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true,
    "link": true
  },
  "dimensions": {
    "__experimentalDefaultControls": {
      "minHeight": false
    },
    "minHeight": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
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
    "__experimentalWritingMode": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/video
**Title:** Video
**Category:** media
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| autoplay | boolean |  | attribute | video | autoplay |
| blob | string |  |  |  |
| caption | rich-text |  | rich-text | figcaption |
| controls | boolean | true | attribute | video | controls |
| id | number |  |  |  |
| loop | boolean |  | attribute | video | loop |
| muted | boolean |  | attribute | video | muted |
| playsInline | boolean |  | attribute | video | playsinline |
| poster | string |  | attribute | video | poster |
| preload | string | metadata | attribute | video | preload |
| src | string |  | attribute | video | src |
| tracks | array | [] |  |  |

### Supports
```json
{
  "align": true,
  "anchor": true,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": false,
      "padding": false
    },
    "margin": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/widget-group
**Title:** Widget Group
**Category:** widgets
**API Version:** 3
**Origin:** core
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| title | string |  |  |  |

### Supports
```json
{
  "customClassName": true,
  "html": false,
  "inserter": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---