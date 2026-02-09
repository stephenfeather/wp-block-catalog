---
wordpress_version: 
generated_at_utc: 2026-02-09T15:02:21Z
---

# WordPress Blocks Catalog ()

## core/legacy-widget
**Title:** Legacy Widget
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| id | string |  |  |  |
| idBase | string |  |  |  |
| instance | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

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
## core/widget-group
**Title:** Widget Group
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
## core/accordion
**Title:** Accordion
**Category:** design
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| ariaLabel | string |  |  |  |
| autoclose | boolean | false |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| headingLevel | number | 3 |  |  |
| iconPosition | string | right |  |  |
| layout | object |  |  |  |
| levelOptions | array |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showIcon | boolean | true |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## core/accordion-item
**Title:** Accordion Item
**Category:** design
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| openByDefault | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## core/archives
**Title:** Archives
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| displayAsDropdown | boolean | false |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showLabel | boolean | true |  |  |
| showPostCounts | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |
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
## core/avatar
**Title:** Avatar
**Category:** theme
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| isLink | boolean | false |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| size | number | 96 |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | object | [] |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| linkTarget | string |  | attribute | a | target |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| placeholder | string |  |  |  |
| rel | string |  | attribute | a | rel |
| style | object |  |  |  |
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
## core/calendar
**Title:** Calendar
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| month | integer |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| displayAsDropdown | boolean | false |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showEmpty | boolean | false |  |  |
| showHierarchy | boolean | false |  |  |
| showLabel | boolean | true |  |  |
| showOnlyTopLevel | boolean | false |  |  |
| showPostCounts | boolean | false |  |  |
| style | object |  |  |  |
| taxonomy | string | category |  |  |
| textColor | string |  |  |  |

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
## core/comment-author-name
**Title:** Comment Author Name
**Category:** theme
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| isLink | boolean | true |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| format | string |  |  |  |
| gradient | string |  |  |  |
| isLink | boolean | true |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
**Origin:** 
**Dynamic:** 

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
| legacy | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| tagName | string | div |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| paginationArrow | string | none |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
**Origin:** 
**Dynamic:** 

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
| level | number | 2 |  |  |
| levelOptions | array |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showCommentsCount | boolean | true |  |  |
| showPostTitle | boolean | true |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alt | string |  |  |  |
| backgroundType | string | image |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| contentPosition | string |  |  |  |
| customGradient | string |  |  |  |
| customOverlayColor | string |  |  |  |
| dimRatio | number | 100 |  |  |
| focalPoint | object |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| hasParallax | boolean | false |  |  |
| id | number |  |  |  |
| isDark | boolean | true |  |  |
| isRepeated | boolean | false |  |  |
| isUserOverlayColor | boolean |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| minHeight | number |  |  |  |
| minHeightUnit | string |  |  |  |
| overlayColor | string |  |  |  |
| poster | string |  | attribute | video | poster |
| sizeSlug | string |  |  |  |
| style | object |  |  |  |
| tagName | string | div |  |  |
| templateLock | ["string", "boolean"] |  |  |  |
| textColor | string |  |  |  |
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
## core/file
**Title:** File
**Category:** media
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| blob | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| displayPreview | boolean |  |  |  |
| downloadButtonText | rich-text |  | rich-text | a[download] |
| fileId | string |  | attribute | a:not([download]) | id |
| fileName | rich-text |  | rich-text | a:not([download]) |
| gradient | string |  |  |  |
| href | string |  |  |  |
| id | number |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| previewHeight | number | 600 |  |  |
| showDownloadButton | boolean | true |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## core/gallery
**Title:** Gallery
**Category:** media
**API Version:** 3
**Origin:** 
**Dynamic:** 

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
## core/heading
**Title:** Heading
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| content | rich-text |  | rich-text | h1,h2,h3,h4,h5,h6 |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| level | number | 2 |  |  |
| levelOptions | array |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| placeholder | string |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
## core/image
**Title:** Image
**Category:** media
**API Version:** 3
**Origin:** 
**Dynamic:** 

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
## core/latest-comments
**Title:** Latest Comments
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| commentsToShow | number | 5 |  |  |
| displayAvatar | boolean | true |  |  |
| displayDate | boolean | true |  |  |
| displayExcerpt | boolean | true |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| addLinkToFeaturedImage | boolean | false |  |  |
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| categories | array |  |  |  |
| className | string |  |  |  |
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
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| order | string | desc |  |  |
| orderBy | string | date |  |  |
| postLayout | string | list |  |  |
| postsToShow | number | 5 |  |  |
| selectedAuthor | number |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## core/list
**Title:** List
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| ordered | boolean | false |  |  |
| placeholder | string |  |  |  |
| reversed | boolean |  |  |  |
| start | number |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |
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
## core/loginout
**Title:** Login/out
**Category:** theme
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| displayLoginAsForm | boolean | false |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| redirectToCurrent | boolean | true |  |  |
| style | object |  |  |  |

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
## core/media-text
**Title:** Media & Text
**Category:** media
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | none |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| focalPoint | object |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| href | string |  | attribute | figure a | href |
| imageFill | boolean |  |  |  |
| isStackedOnMobile | boolean | true |  |  |
| linkClass | string |  | attribute | figure a | class |
| linkDestination | string |  |  |  |
| linkTarget | string |  | attribute | figure a | target |
| lock | object |  |  |  |
| mediaAlt | string |  | attribute | figure img | alt |
| mediaId | number |  |  |  |
| mediaLink | string |  |  |  |
| mediaPosition | string | left |  |  |
| mediaSizeSlug | string |  |  |  |
| mediaType | string |  |  |  |
| mediaUrl | string |  | attribute | figure video,figure img | src |
| mediaWidth | number | 50 |  |  |
| metadata | object |  |  |  |
| rel | string |  | attribute | figure a | rel |
| style | object |  |  |  |
| textColor | string |  |  |  |
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
## core/navigation
**Title:** Navigation
**Category:** theme
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| __unstableLocation | string |  |  |  |
| align | string |  |  |  |
| ariaLabel | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| customBackgroundColor | string |  |  |  |
| customOverlayBackgroundColor | string |  |  |  |
| customOverlayTextColor | string |  |  |  |
| customTextColor | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| hasIcon | boolean | true |  |  |
| icon | string | handle |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| maxNestingLevel | number | 5 |  |  |
| metadata | object |  |  |  |
| openSubmenusOnClick | boolean | false |  |  |
| overlayBackgroundColor | string |  |  |  |
| overlayMenu | string | mobile |  |  |
| overlayTextColor | string |  |  |  |
| ref | number |  |  |  |
| rgbBackgroundColor | string |  |  |  |
| rgbTextColor | string |  |  |  |
| showSubmenuIcon | boolean | true |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| description | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| id | number |  |  |  |
| isTopLevelLink | boolean |  |  |  |
| kind | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| opensInNewTab | boolean | false |  |  |
| rel | string |  |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| description | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| id | number |  |  |  |
| isTopLevelItem | boolean |  |  |  |
| kind | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| opensInNewTab | boolean | false |  |  |
| rel | string |  |  |  |
| style | object |  |  |  |
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
## core/page-list
**Title:** Page List
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| isNested | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| parentPageID | integer | 0 |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| hasChildren | boolean |  |  |  |
| id | number |  |  |  |
| label | string |  |  |  |
| link | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
## core/pattern
**Title:** Pattern Placeholder
**Category:** theme
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| avatarSize | number | 48 |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| byline | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| isLink | boolean | false |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showAvatar | boolean | true |  |  |
| showBio | boolean |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| isLink | boolean | false |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

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
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| tagName | string | div |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| datetime | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| format | string |  |  |  |
| gradient | string |  |  |  |
| isLink | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| excerptLength | number | 55 |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| moreText | string |  |  |  |
| showMoreOnNewLine | boolean | true |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| aspectRatio | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| customGradient | string |  |  |  |
| customOverlayColor | string |  |  |  |
| dimRatio | number | 0 |  |  |
| gradient | string |  |  |  |
| height | string |  |  |  |
| isLink | boolean | false |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| overlayColor | string |  |  |  |
| rel | string |  |  | rel |
| scale | string | cover |  |  |
| sizeSlug | string |  |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| arrow | string | none |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| label | string |  |  |  |
| linkLabel | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showTitle | boolean | false |  |  |
| style | object |  |  |  |
| taxonomy | string |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |
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
**Origin:** 
**Dynamic:** 

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
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| prefix | string |  |  |  |
| separator | string | ,  |  |  |
| style | object |  |  |  |
| suffix | string |  |  |  |
| term | string |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| averageReadingSpeed | number | 189 |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| displayAsRange | boolean | true |  |  |
| displayMode | string | time |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

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
| isLink | boolean | false |  |  |
| level | number | 2 |  |  |
| levelOptions | array |  |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| rel | string |  |  | rel |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
## core/query
**Title:** Query Loop
**Category:** theme
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| enhancedPagination | boolean | false |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| paginationArrow | string | none |  |  |
| showLabel | boolean | true |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| midSize | number | 2 |  |  |
| style | object |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
**Origin:** 
**Dynamic:** 

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
| level | number | 1 |  |  |
| levelOptions | array |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showPrefix | boolean | true |  |  |
| showSearchTerm | boolean | true |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| displayType | string | total-results |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## core/read-more
**Title:** Read More
**Category:** theme
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| content | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| blockLayout | string | list |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| columns | number | 2 |  |  |
| displayAuthor | boolean | false |  |  |
| displayDate | boolean | false |  |  |
| displayExcerpt | boolean | false |  |  |
| excerptLength | number | 55 |  |  |
| feedURL | string |  |  |  |
| gradient | string |  |  |  |
| itemsToShow | number | 5 |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| openInNewTab | boolean | false |  |  |
| rel | string |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| buttonPosition | string | button-outside |  |  |
| buttonText | string |  |  |  |
| buttonUseIcon | boolean | false |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| isSearchFieldHidden | boolean | false |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| placeholder | string |  |  |  |
| query | object | [] |  |  |
| showLabel | boolean | true |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |
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
## core/shortcode
**Title:** Shortcode
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| isLink | boolean | true |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| shouldSyncIcon | boolean |  |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

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
| level | number | 0 |  |  |
| levelOptions | array | [0, 1, 2, 3, 4, 5, 6] |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

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
| isLink | boolean | true |  |  |
| level | number | 1 |  |  |
| levelOptions | array | [0, 1, 2, 3, 4, 5, 6] |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
## core/tag-cloud
**Title:** Tag Cloud
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| largestFontSize | string | 22pt |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| numberOfTags | number | 45 |  |  |
| showTagCounts | boolean | false |  |  |
| smallestFontSize | string | 8pt |  |  |
| style | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| area | string |  |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| bracketType | string | round |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

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
| isLink | boolean | false |  |  |
| level | number | 0 |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

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
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## core/video
**Title:** Video
**Category:** media
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| autoplay | boolean |  | attribute | video | autoplay |
| blob | string |  |  |  |
| caption | rich-text |  | rich-text | figcaption |
| className | string |  |  |  |
| controls | boolean | true | attribute | video | controls |
| id | number |  |  |  |
| lock | object |  |  |  |
| loop | boolean |  | attribute | video | loop |
| metadata | object |  |  |  |
| muted | boolean |  | attribute | video | muted |
| playsInline | boolean |  | attribute | video | playsinline |
| poster | string |  | attribute | video | poster |
| preload | string | metadata | attribute | video | preload |
| src | string |  | attribute | video | src |
| style | object |  |  |  |
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
## core/accordion-heading
**Title:** Accordion Heading
**Category:** design
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| iconPosition | string | right |  |  |
| level | number |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| openByDefault | boolean | false |  |  |
| showIcon | boolean | true |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |
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
## core/accordion-panel
**Title:** Accordion Panel
**Category:** design
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| isSelected | boolean | false |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| openByDefault | boolean | false |  |  |
| style | object |  |  |  |
| templateLock | ["string", "boolean"] | false |  |  |
| textColor | string |  |  |  |

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
## core/audio
**Title:** Audio
**Category:** media
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| autoplay | boolean |  | attribute | audio | autoplay |
| blob | string |  |  |  |
| caption | rich-text |  | rich-text | figcaption |
| className | string |  |  |  |
| id | number |  |  |  |
| lock | object |  |  |  |
| loop | boolean |  | attribute | audio | loop |
| metadata | object |  |  |  |
| preload | string |  | attribute | audio | preload |
| src | string |  | attribute | audio | src |
| style | object |  |  |  |

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
## core/buttons
**Title:** Buttons
**Category:** design
**API Version:** 3
**Origin:** 
**Dynamic:** 

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
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
## core/code
**Title:** Code
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| content | rich-text |  | rich-text | code |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| templateLock | ["string", "boolean"] |  |  |  |
| textColor | string |  |  |  |
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
**Origin:** 
**Dynamic:** 

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
## core/details
**Title:** Details
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

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
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| name | string |  | attribute | .wp-block-details | name |
| placeholder | string |  |  |  |
| showContent | boolean | false |  |  |
| style | object |  |  |  |
| summary | rich-text |  | rich-text | summary |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| allowResponsive | boolean | true |  |  |
| caption | rich-text |  | rich-text | figcaption |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| previewable | boolean | true |  |  |
| providerNameSlug | string |  |  |  |
| responsive | boolean | false |  |  |
| style | object |  |  |  |
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
## core/freeform
**Title:** Classic
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  | raw |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

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
## core/group
**Title:** Group
**Category:** design
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| ariaLabel | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| tagName | string | div |  |  |
| templateLock | ["string", "boolean"] |  |  |  |
| textColor | string |  |  |  |

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
## core/html
**Title:** Custom HTML
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  | raw |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

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
## core/list-item
**Title:** List Item
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| content | rich-text |  | rich-text | li |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| placeholder | string |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## core/math
**Title:** Math
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| latex | string |  |  |  |
| lock | object |  |  |  |
| mathML | string |  | html | math |
| metadata | object |  |  |  |

### Supports
```json
{
  "html": false
}
```

### Example Markup
_Not generated yet._

---
## core/missing
**Title:** Unsupported
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| customText | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
## core/nextpage
**Title:** Page Break
**Category:** design
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object |  |  |  |
| metadata | object |  |  |  |

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
## core/paragraph
**Title:** Paragraph
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| content | rich-text |  | rich-text | p |
| direction | string |  |  |  |
| dropCap | boolean | false |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| placeholder | string |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## core/preformatted
**Title:** Preformatted
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| content | rich-text |  | rich-text | pre |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| citation | rich-text |  | rich-text | cite |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |
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
## core/quote
**Title:** Quote
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| citation | rich-text |  | rich-text | cite |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |
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
## core/separator
**Title:** Separator
**Category:** design
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| opacity | string | alpha-channel |  |  |
| style | object |  |  |  |
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
## core/social-links
**Title:** Social Icons
**Category:** widgets
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| customIconBackgroundColor | string |  |  |  |
| customIconColor | string |  |  |  |
| gradient | string |  |  |  |
| iconBackgroundColor | string |  |  |  |
| iconBackgroundColorValue | string |  |  |  |
| iconColor | string |  |  |  |
| iconColorValue | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| openInNewTab | boolean | false |  |  |
| showLabels | boolean | false |  |  |
| size | string |  |  |  |
| style | object |  |  |  |

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
**Origin:** 
**Dynamic:** 

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
## core/table
**Title:** Table
**Category:** text
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| body | array | [] | query | tbody tr |
| borderColor | string |  |  |  |
| caption | rich-text |  | rich-text | figcaption |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| foot | array | [] | query | tfoot tr |
| gradient | string |  |  |  |
| hasFixedLayout | boolean | true |  |  |
| head | array | [] | query | thead tr |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## core/terms-query
**Title:** Terms Query
**Category:** theme
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| columns | number | 2 |  |  |
| content | array | [[], []] | query | p |
| lock | object |  |  |  |
| metadata | object |  |  |  |
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
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| content | rich-text |  | rich-text | pre |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
## woocommerce/active-filters
**Title:** Active Filters Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| displayStyle | string | list |  |  |
| headingLevel | number | 3 |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": false,
    "text": true
  },
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  },
  "lock": false,
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-form
**Title:** Add to Cart with Options
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| quantitySelectorStyle | string | input |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/all-products
**Title:** All Products
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean |  |  |  |
| className | string |  |  |  |
| columns | number |  |  |  |
| contentVisibility | object |  |  |  |
| isPreview | boolean | false |  |  |
| layoutConfig | array |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| orderby | string |  |  |  |
| rows | number |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  },
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/all-reviews
**Title:** All Reviews
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/attribute-filter
**Title:** Filter by Attribute Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| attributeId | number | 0 |  |  |
| className | string |  |  |  |
| displayStyle | string | list |  |  |
| headingLevel | number | 3 |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| queryType | string | or |  |  |
| selectType | string | multiple |  |  |
| showCounts | boolean | false |  |  |
| showFilterButton | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": false,
    "text": true
  },
  "html": false,
  "inserter": false,
  "interactivity": false,
  "lock": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/breadcrumbs
**Title:** Store Breadcrumbs
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |
| contentJustification | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string | small |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "background": false,
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
    "__experimentalTextTransform": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-link
**Title:** Cart Link
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| cartIcon | string | cart |  |  |
| className | string |  |  |  |
| content | string |  |  |  |
| fontSize | string |  |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "color": {
    "link": true,
    "text": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "multiple": false,
  "spacing": {
    "padding": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/catalog-sorting
**Title:** Catalog Sorting
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontSize | string | small |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |
| useLabel | boolean | false |  |  |

### Supports
```json
{
  "color": {
    "background": false,
    "text": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/category-title
**Title:** Product Category Title
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| isLink | boolean | false |  |  |
| level | number | 2 |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| rel | string |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": false,
  "color": {
    "background": true,
    "text": true
  },
  "html": false,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/category-description
**Title:** Product Category Description
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": false,
  "color": {
    "background": true,
    "text": true
  },
  "html": false,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/legacy-template
**Title:** 
**Category:** 
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
_None_

### Example Markup
_Not generated yet._

---
## woocommerce/classic-shortcode
**Title:** Classic Shortcode
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

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
## woocommerce/coming-soon
**Title:** Coming Soon
**Category:** woocommerce
**API Version:** 1
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| color | string |  |  |  |
| comingSoonPatternId | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| storeOnly | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": true,
    "text": true
  },
  "inserter": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/coupon-code
**Title:** Coupon Code
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| couponCode | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "text": true
  },
  "email": true,
  "html": false,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/customer-account
**Title:** Customer account
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| displayStyle | string | icon_and_text |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| iconClass | string | icon |  |  |
| iconStyle | string | default |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": true,
  "color": {
    "text": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalFontFamily": true,
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/email-content
**Title:** Email Content
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| emailType | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| postId | integer |  |  |  |

### Supports
```json
{
  "email": true,
  "inserter": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/featured-category
**Title:** Featured Category
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alt | string |  |  |  |
| ariaLabel | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| categoryId | number |  |  |  |
| className | string |  |  |  |
| contentAlign | string | center |  |  |
| dimRatio | number | 50 |  |  |
| focalPoint | object | {"x": 0.5, "y": 0.5} |  |  |
| hasParallax | boolean | false |  |  |
| imageFit | string | none |  |  |
| isRepeated | boolean | false |  |  |
| linkText | string | Shop now |  |  |
| lock | object |  |  |  |
| mediaId | number | 0 |  |  |
| mediaSrc | string |  |  |  |
| metadata | object |  |  |  |
| minHeight | number | 500 |  |  |
| overlayColor | string | #000000 |  |  |
| overlayGradient | string |  |  |  |
| previewCategory | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "wide",
    "full"
  ],
  "ariaLabel": true,
  "color": {
    "background": true,
    "text": true
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
      "padding": true
    },
    "__experimentalSkipSerialization": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/featured-product
**Title:** Featured Product
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alt | string |  |  |  |
| ariaLabel | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| contentAlign | string | center |  |  |
| dimRatio | number | 50 |  |  |
| focalPoint | object | {"x": 0.5, "y": 0.5} |  |  |
| hasParallax | boolean | false |  |  |
| imageFit | string | none |  |  |
| isRepeated | boolean | false |  |  |
| linkText | string | Shop now |  |  |
| lock | object |  |  |  |
| mediaId | number | 0 |  |  |
| mediaSrc | string |  |  |  |
| metadata | object |  |  |  |
| minHeight | number | 500 |  |  |
| overlayColor | string | #000000 |  |  |
| overlayGradient | string |  |  |  |
| previewProduct | object |  |  |  |
| productId | number |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "wide",
    "full"
  ],
  "ariaLabel": true,
  "color": {
    "background": true,
    "text": true
  },
  "filter": {
    "duotone": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "multiple": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "padding": true
    },
    "__experimentalSkipSerialization": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/filter-wrapper
**Title:** Filter Block
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| filterType | string |  |  |  |
| heading | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/handpicked-products
**Title:** Hand-picked Products
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean | false |  |  |
| className | string |  |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| orderby | string | date |  |  |
| products | array | [] |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart
**Title:** Mini-Cart
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| addToCartBehaviour | string | none |  |  |
| cartAndCheckoutRenderStyle | string | hidden |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| hasHiddenPrice | boolean | true |  |  |
| iconColor | object |  |  |  |
| iconColorValue | string |  |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| miniCartIcon | string | cart |  |  |
| onCartClickBehaviour | string | open_drawer |  |  |
| priceColor | object |  |  |  |
| priceColorValue | string |  |  |  |
| productCountColor | object |  |  |  |
| productCountColorValue | string |  |  |  |
| productCountVisibility | string | greater_than_zero |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "html": false,
  "interactivity": true,
  "multiple": false,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-gallery-large-image-next-previous
**Title:** Next/Previous Buttons
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalSkipSerialization": true,
    "radius": true
  },
  "__experimentalSelector": ".wc-block-next-previous-buttons__button",
  "align": true,
  "color": {
    "__experimentalSkipSerialization": true,
    "background": true,
    "text": true
  },
  "interactivity": true,
  "layout": {
    "allowJustification": false,
    "allowOrientation": false,
    "allowVerticalAlignment": true,
    "default": {
      "flexWrap": "nowrap",
      "type": "flex",
      "verticalAlignment": "center"
    }
  },
  "shadow": true,
  "spacing": {
    "__experimentalSkipSerialization": true,
    "margin": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/store-notices
**Title:** Store Notices
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "interactivity": {
    "clientNavigation": true
  },
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/payment-method-icons
**Title:** Payment Method Icons
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| numberOfIcons | number | 0 |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "spacing": {
    "margin": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/price-filter
**Title:** Filter by Price Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| headingLevel | number | 3 |  |  |
| inlineInput | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showFilterButton | boolean | false |  |  |
| showInputFields | boolean | true |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": false,
    "text": true
  },
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  },
  "lock": false,
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-best-sellers
**Title:** Best Selling Products
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| className | string |  |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| editMode | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| orderby | string | popularity |  |  |
| rows | number | 3 |  |  |
| stockStatus | array |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-button
**Title:** Add to Cart Button
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number | 0 |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |
| width | number |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalSkipSerialization": true,
    "radius": true
  },
  "__experimentalSelector": ".wp-block-button.wc-block-components-product-button .wc-block-components-product-button__button",
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "__experimentalSkipSerialization": true,
    "background": true,
    "link": false,
    "text": true
  },
  "email": true,
  "html": false,
  "interactivity": true,
  "spacing": {
    "__experimentalSkipSerialization": true,
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
## woocommerce/product-categories
**Title:** Product Categories List
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| hasCount | boolean | true |  |  |
| hasEmpty | boolean | false |  |  |
| hasImage | boolean | false |  |  |
| isDropdown | boolean | false |  |  |
| isHierarchical | boolean | true |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showChildrenOnly | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "background": false,
    "link": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "typography": {
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-category
**Title:** Products by Category
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| className | string |  |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| editMode | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| orderby | string | date |  |  |
| rows | number | 3 |  |  |
| stockStatus | array |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-collection
**Title:** Product Collection
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| __privatePreviewState | object |  |  |  |
| align | string |  |  |  |
| className | string |  |  |  |
| collection | string |  |  |  |
| convertedFromProducts | boolean | false |  |  |
| dimensions | object |  |  |  |
| displayLayout | object |  |  |  |
| forcePageReload | boolean | false |  |  |
| hideControls | array | [] |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| query | object |  |  |  |
| queryContextIncludes | array |  |  |  |
| queryId | number |  |  |  |
| tagName | string |  |  |  |

### Supports
```json
{
  "__experimentalLayout": true,
  "align": [
    "wide",
    "full"
  ],
  "anchor": true,
  "email": true,
  "html": false,
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-collection-no-results
**Title:** No results
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": true,
  "color": {
    "gradients": true,
    "link": true
  },
  "email": true,
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
## woocommerce/product-filters
**Title:** Product Filters
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| isPreview | boolean | false |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": true,
  "color": {
    "background": true,
    "button": true,
    "enableContrastChecker": false,
    "heading": true,
    "text": true
  },
  "inserter": true,
  "interactivity": true,
  "layout": {
    "allowEditing": false,
    "default": {
      "flexWrap": "nowrap",
      "justifyContent": "stretch",
      "orientation": "vertical",
      "type": "flex"
    }
  },
  "multiple": true,
  "spacing": {
    "blockGap": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-status
**Title:** Status Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| borderColor | string |  |  |  |
| className | string |  |  |  |
| displayStyle | string | woocommerce/product-filter-checkbox-list |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| hideEmpty | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showCounts | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
      "text": false
    },
    "background": false,
    "text": true
  },
  "html": false,
  "interactivity": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": false,
      "margin": false,
      "padding": false
    },
    "blockGap": true,
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": false
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
## woocommerce/product-filter-price
**Title:** Price Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "html": false,
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-price-slider
**Title:** Price Slider
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| customSlider | string |  |  |  |
| customSliderHandle | string |  |  |  |
| customSliderHandleBorder | string |  |  |  |
| inlineInput | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showInputFields | boolean | true |  |  |
| slider | string |  |  |  |
| sliderHandle | string |  |  |  |
| sliderHandleBorder | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": false,
    "enableContrastChecker": false,
    "text": false
  },
  "html": false,
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-attribute
**Title:** Attribute Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| attributeId | number | 0 |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| displayStyle | string | woocommerce/product-filter-checkbox-list |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| hideEmpty | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| queryType | string | or |  |  |
| selectType | string | multiple |  |  |
| showCounts | boolean | false |  |  |
| sortOrder | string | count-desc |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
      "text": false
    },
    "background": false,
    "text": true
  },
  "interactivity": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": false,
      "margin": false,
      "padding": false
    },
    "blockGap": true,
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": false
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
## woocommerce/product-filter-rating
**Title:** Rating Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| minRating | string | 0 |  |  |
| showCounts | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": false,
    "text": true
  },
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-active
**Title:** Active Filters
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| borderColor | string |  |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
  "interactivity": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": false,
      "margin": false,
      "padding": false
    },
    "blockGap": false,
    "margin": true,
    "padding": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-removable-chips
**Title:** Chips
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| chipBackground | string |  |  |  |
| chipBorder | string |  |  |  |
| chipText | string |  |  |  |
| className | string |  |  |  |
| customChipBackground | string |  |  |  |
| customChipBorder | string |  |  |  |
| customChipText | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "interactivity": true,
  "layout": {
    "allowInheriting": false,
    "allowSwitching": false,
    "allowVerticalAlignment": false,
    "default": {
      "type": "flex"
    }
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-clear-button
**Title:** Clear filters
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "inserter": true,
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-checkbox-list
**Title:** List
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| customLabelElement | string |  |  |  |
| customOptionElement | string |  |  |  |
| customOptionElementBorder | string |  |  |  |
| customOptionElementSelected | string |  |  |  |
| labelElement | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| optionElement | string |  |  |  |
| optionElementBorder | string |  |  |  |
| optionElementSelected | string |  |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-chips
**Title:** Chips
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| chipBackground | string |  |  |  |
| chipBorder | string |  |  |  |
| chipText | string |  |  |  |
| className | string |  |  |  |
| customChipBackground | string |  |  |  |
| customChipBorder | string |  |  |  |
| customChipText | string |  |  |  |
| customSelectedChipBackground | string |  |  |  |
| customSelectedChipBorder | string |  |  |  |
| customSelectedChipText | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| selectedChipBackground | string |  |  |  |
| selectedChipBorder | string |  |  |  |
| selectedChipText | string |  |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-taxonomy
**Title:** Taxonomy Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| borderColor | string |  |  |  |
| className | string |  |  |  |
| displayStyle | string | woocommerce/product-filter-checkbox-list |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| hideEmpty | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showCounts | boolean | false |  |  |
| sortOrder | string | count-desc |  |  |
| style | object |  |  |  |
| taxonomy | string | product_cat |  |  |
| textColor | string |  |  |  |

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
      "text": false
    },
    "background": false,
    "text": true
  },
  "interactivity": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "blockGap": false,
      "margin": false,
      "padding": false
    },
    "blockGap": true,
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": false
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
## woocommerce/product-gallery
**Title:** Product Gallery
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| fullScreenOnClick | boolean | true |  |  |
| hoverZoom | boolean | true |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": true,
  "email": true,
  "interactivity": true,
  "layout": {
    "allowEditing": true,
    "allowJustification": false,
    "allowOrientation": true,
    "default": {
      "flexWrap": "nowrap",
      "orientation": "horizontal",
      "type": "flex"
    }
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-gallery-large-image
**Title:** Viewer
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-gallery-thumbnails
**Title:** Thumbnails
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| activeThumbnailStyle | string | overlay |  |  |
| aspectRatio | string | 1 |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| thumbnailSize | string | 25% |  |  |

### Supports
```json
{
  "interactivity": true,
  "spacing": {
    "margin": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-image
**Title:** Product Image
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| aspectRatio | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| height | string |  |  |  |
| imageSizing | string | single |  |  |
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number | 0 |  |  |
| saleBadgeAlign | string | right |  |  |
| scale | string | cover |  |  |
| showProductLink | boolean | true |  |  |
| showSaleBadge | boolean | true |  |  |
| style | object |  |  |  |
| width | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalSkipSerialization": true,
    "radius": true
  },
  "__experimentalSelector": ".wc-block-components-product-image",
  "dimensions": {
    "__experimentalSkipSerialization": true,
    "aspectRatio": true
  },
  "email": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalSkipSerialization": true,
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-image-gallery
**Title:** Product Image Gallery
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": true,
  "interactivity": {
    "clientNavigation": true
  },
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-meta
**Title:** Product Meta
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": true,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-new
**Title:** Newest Products
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| className | string |  |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| editMode | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| orderby | string | date |  |  |
| rows | number | 3 |  |  |
| stockStatus | array |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-on-sale
**Title:** On Sale Products
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| className | string |  |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| orderby | string | date |  |  |
| rows | number | 3 |  |  |
| stockStatus | array |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-price
**Title:** Product Price
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number | 0 |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "__experimentalSelector": ".wp-block-woocommerce-product-price .wc-block-components-product-price",
  "color": {
    "background": true,
    "link": false,
    "text": true
  },
  "email": true,
  "html": false,
  "interactivity": true,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-template
**Title:** Product Template
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
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
    "gradients": true,
    "link": true
  },
  "email": true,
  "html": false,
  "inserter": false,
  "interactivity": true,
  "layout": {
    "allowEditing": false,
    "allowInheriting": false,
    "allowSizingOnChildren": false,
    "allowSwitching": false,
    "allowVerticalAlignment": false
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
## woocommerce/product-query
**Title:** 
**Category:** 
**API Version:** 1
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
_None_

### Example Markup
_Not generated yet._

---
## woocommerce/product-average-rating
**Title:** Product Average Rating (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "__experimentalSelector": ".wc-block-components-product-average-rating",
  "color": {
    "__experimentalSkipSerialization": true,
    "background": true,
    "text": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "__experimentalSkipSerialization": true,
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalFontWeight": true,
    "__experimentalSkipSerialization": true,
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-rating
**Title:** Product Rating
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontSize | string |  |  |  |
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number | 0 |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "__experimentalSelector": ".wc-block-components-product-rating",
  "color": {
    "__experimentalSkipSerialization": true,
    "background": false,
    "link": false,
    "text": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalSkipSerialization": true,
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-rating-counter
**Title:** Product Rating Counter
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontSize | string |  |  |  |
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number | 0 |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |

### Supports
```json
{
  "__experimentalSelector": ".wc-block-components-product-rating-counter",
  "color": {
    "background": false,
    "link": true,
    "text": false
  },
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalSkipSerialization": true,
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-rating-stars
**Title:** Product Rating Stars
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontSize | string |  |  |  |
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number | 0 |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "__experimentalSelector": ".wc-block-components-product-rating",
  "color": {
    "__experimentalSkipSerialization": true,
    "background": false,
    "link": false,
    "text": true
  },
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalSkipSerialization": true,
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-results-count
**Title:** Product Results Count
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": false,
    "text": true
  },
  "interactivity": {
    "clientNavigation": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-sale-badge
**Title:** On-Sale Badge
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

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
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number | 0 |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "__experimentalSkipSerialization": true,
    "color": true,
    "radius": true,
    "width": true
  },
  "__experimentalSelector": ".wc-block-components-product-sale-badge",
  "align": true,
  "color": {
    "__experimentalSkipSerialization": true,
    "background": true,
    "gradients": true,
    "link": false
  },
  "email": true,
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "spacing": {
    "margin": true
  },
  "typography": {
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
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
## woocommerce/product-search
**Title:** 
**Category:** 
**API Version:** 1
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
_None_

### Example Markup
_Not generated yet._

---
## woocommerce/product-sku
**Title:** Product SKU
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| isDescendantOfAllProducts | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| prefix | string | SKU: |  |  |
| productId | number | 0 |  |  |
| showProductSelector | boolean | false |  |  |
| style | object |  |  |  |
| suffix | string |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": true,
    "text": true
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
## woocommerce/product-stock-indicator
**Title:** Product Stock Indicator
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| isDescendantOfAllProducts | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": true,
    "text": true
  },
  "html": false,
  "interactivity": true,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
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
## woocommerce/product-summary
**Title:** Product Summary
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| isDescendantOfAllProducts | boolean | false |  |  |
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| linkText | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number | 0 |  |  |
| showDescriptionIfEmpty | boolean | false |  |  |
| showLink | boolean | false |  |  |
| style | object |  |  |  |
| summaryLength | number | 0 |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "__experimentalSelector": ".wc-block-components-product-summary",
  "color": {
    "background": true,
    "link": true,
    "text": true
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
    "lineHeight": true,
    "textAlign": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-tag
**Title:** Products by Tag
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean | false |  |  |
| className | string |  |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| orderby | string | date |  |  |
| rows | number | 3 |  |  |
| stockStatus | array |  |  |  |
| tagOperator | string | any |  |  |
| tags | array | [] |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-title
**Title:** Product Title
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| headingLevel | number | 2 |  |  |
| linkTarget | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number | 0 |  |  |
| showProductLink | boolean | true |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "__experimentalSelector": ".wc-block-components-product-title",
  "color": {
    "__experimentalSkipSerialization": true,
    "background": true,
    "gradients": true,
    "link": false,
    "text": true
  },
  "html": false,
  "interactivity": {
    "clientNavigation": false
  },
  "spacing": {
    "__experimentalSkipSerialization": true,
    "margin": true
  },
  "typography": {
    "__experimentalFontFamily": true,
    "__experimentalFontWeight": true,
    "__experimentalTextTransform": true,
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-top-rated
**Title:** Top Rated Products
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| className | string |  |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| editMode | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| orderby | string | rating |  |  |
| rows | number | 3 |  |  |
| stockStatus | array |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/products-by-attribute
**Title:** Products by Attribute
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean | false |  |  |
| attrOperator | string | any |  |  |
| attributes | array | [] |  |  |
| className | string |  |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| orderby | string | date |  |  |
| rows | number | 3 |  |  |
| stockStatus | array |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/rating-filter
**Title:** Filter by Rating Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| displayStyle | string | list |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| selectType | string | multiple |  |  |
| showCounts | boolean | false |  |  |
| showFilterButton | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": true,
    "button": true,
    "text": true
  },
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  },
  "lock": false,
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/reviews-by-category
**Title:** Reviews by Category
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/reviews-by-product
**Title:** Reviews by Product
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": false
  },
  "html": false,
  "interactivity": {
    "clientNavigation": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/related-products
**Title:** Related Products
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": true,
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/single-product
**Title:** Product
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| productId | number |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/stock-filter
**Title:** Filter by Stock Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| displayStyle | string | list |  |  |
| headingLevel | number | 3 |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| selectType | string | multiple |  |  |
| showCounts | boolean | false |  |  |
| showFilterButton | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "background": true,
    "button": true,
    "text": true
  },
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": false
  },
  "lock": false,
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/page-content-wrapper
**Title:** WooCommerce Page
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| page | string |  |  |  |

### Supports
```json
{
  "html": false,
  "inserter": false,
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/order-confirmation-status
**Title:** Order Status
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "background": true,
    "gradients": true,
    "text": true
  },
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-summary
**Title:** Order Summary
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "background": true,
    "gradients": true,
    "text": true
  },
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-totals
**Title:** Order Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "style": true,
    "width": true
  },
  "__experimentalSelector": ".wp-block-woocommerce-order-confirmation-totals table",
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "background": true,
    "gradients": true,
    "link": true,
    "text": true
  },
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-totals-wrapper
**Title:** Order Totals Section
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| heading | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-downloads
**Title:** Order Downloads
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "style": true,
    "width": true
  },
  "__experimentalSelector": ".wp-block-woocommerce-order-confirmation-totals table",
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "background": true,
    "gradients": true,
    "link": true,
    "text": true
  },
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-downloads-wrapper
**Title:** Downloads Section
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| heading | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-billing-address
**Title:** Billing Address
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "wide",
    "full"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "background": true,
    "text": true
  },
  "html": false,
  "inserter": false,
  "multiple": false,
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
## woocommerce/order-confirmation-shipping-address
**Title:** Shipping Address
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "wide",
    "full"
  ],
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "background": true,
    "text": true
  },
  "html": false,
  "inserter": false,
  "multiple": false,
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
## woocommerce/order-confirmation-billing-wrapper
**Title:** Billing Address Section
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| heading | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-shipping-wrapper
**Title:** Shipping Address Section
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| heading | string | Shipping |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-additional-information
**Title:** Additional Information
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
    "wide",
    "full"
  ],
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-additional-fields-wrapper
**Title:** Additional Fields
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| heading | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-additional-fields
**Title:** Additional Field List
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
    "wide",
    "full"
  ],
  "html": false,
  "multiple": false,
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
## woocommerce/order-confirmation-create-account
**Title:** Account Creation
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| customerEmail | string |  |  |  |
| hasDarkControls | boolean | false |  |  |
| lock | object | {"remove": true} |  |  |
| metadata | object |  |  |  |
| nonceToken | string |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "color": {
    "background": true,
    "button": true,
    "text": true
  },
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
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
## woocommerce/product-details
**Title:** Product Details
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |
| hideTabTitle | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "interactivity": {
    "clientNavigation": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-description
**Title:** Product Description
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

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
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## woocommerce/product-specifications
**Title:** Product Specifications
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showAttributes | boolean | true |  |  |
| showDimensions | boolean | true |  |  |
| showWeight | boolean | true |  |  |
| style | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide",
    "full"
  ],
  "html": false,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
    "fontSize": true,
    "lineHeight": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/accordion-group
**Title:** Accordion Group
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| allowedBlocks | array |  |  |  |
| autoclose | boolean | false |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| iconPosition | string | right |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "background": true,
    "gradient": true
  },
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
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/accordion-item
**Title:** Accordion
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| openByDefault | boolean | false |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "background": true,
    "gradient": true
  },
  "interactivity": true,
  "layout": true,
  "shadow": true,
  "spacing": {
    "blockGap": true,
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
## woocommerce/accordion-panel
**Title:** Accordion Panel
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| allowedBlocks | array |  |  |  |
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| isSelected | boolean | false |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| openByDefault | boolean | false |  |  |
| style | object |  |  |  |
| templateLock | ["string", "boolean"] | false |  |  |
| textColor | string |  |  |  |

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
  "border": true,
  "color": {
    "background": true,
    "gradient": true
  },
  "interactivity": true,
  "layout": true,
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
## woocommerce/accordion-header
**Title:** Accordion Header
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| icon | ["string", "boolean"] | plus |  |  |
| iconPosition | string | right |  |  |
| layout | object |  |  |  |
| level | number | 3 |  |  |
| levelOptions | array |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| openByDefault | boolean | false |  |  |
| style | object |  |  |  |
| textAlignment | string | left |  |  |
| textColor | string |  |  |  |
| title | rich-text |  | rich-text | span |

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
  "border": true,
  "color": {
    "background": true,
    "gradient": true
  },
  "interactivity": true,
  "layout": true,
  "shadow": true,
  "spacing": {
    "__experimentalDefaultControls": {
      "margin": true,
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
      "fontFamily": true,
      "fontSize": true
    },
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalTextDecoration": true,
    "__experimentalTextTransform": true,
    "fontSize": true,
    "textAlign": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-reviews
**Title:** Product Reviews
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

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
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| tagName | string | div |  |  |
| textColor | string |  |  |  |

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
  "interactivity": true,
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
## woocommerce/product-review-rating
**Title:** Review Rating
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "gradients": true
  },
  "interactivity": {
    "clientNavigation": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-reviews-title
**Title:** Reviews Title
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

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
| level | number | 2 |  |  |
| levelOptions | array |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showProductTitle | boolean | true |  |  |
| showReviewsCount | boolean | true |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
## woocommerce/product-review-form
**Title:** Reviews Form
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
  "interactivity": true,
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
## woocommerce/product-review-date
**Title:** Review Date
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| format | string |  |  |  |
| gradient | string |  |  |  |
| isLink | boolean | true |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## woocommerce/product-review-content
**Title:** Review Content
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
## woocommerce/product-review-author-name
**Title:** Review Author Name
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| isLink | boolean | true |  |  |
| linkTarget | string | _self |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

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
## woocommerce/product-reviews-pagination
**Title:** Reviews Pagination
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| paginationArrow | string | none |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
## woocommerce/product-reviews-pagination-next
**Title:** Reviews Next Page
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
## woocommerce/product-reviews-pagination-previous
**Title:** Reviews Previous Page
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
## woocommerce/product-reviews-pagination-numbers
**Title:** Reviews Page Numbers
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
## woocommerce/product-review-template
**Title:** Reviews Template
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |

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
## woocommerce/cart
**Title:** 
**Category:** 
**API Version:** 1
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
_None_

### Example Markup
_Not generated yet._

---
## woocommerce/cart-order-summary-taxes-block
**Title:** Taxes
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-order-summary-subtotal-block
**Title:** Subtotal
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-order-summary-totals-block
**Title:** Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/filled-cart-block
**Title:** Filled Cart
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide"
  ],
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/empty-cart-block
**Title:** Empty Cart
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": [
    "wide"
  ],
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-totals-block
**Title:** Cart Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkbox | boolean | false |  |  |
| className | string |  |  |  |
| lock | object | {"remove": true} |  |  |
| metadata | object |  |  |  |
| text | string |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-items-block
**Title:** Cart Items
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-line-items-block
**Title:** Cart Line Items
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-order-summary-block
**Title:** Order Summary
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-express-payment-block
**Title:** Express Checkout
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| buttonBorderRadius | string | 4 |  |  |
| buttonHeight | string | 48 |  |  |
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |
| showButtonStyles | boolean | false |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/proceed-to-checkout-block
**Title:** Proceed to Checkout
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-accepted-payment-methods-block
**Title:** Accepted Payment Methods
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": true,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-order-summary-coupon-form-block
**Title:** Coupon Form
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": false} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-order-summary-discount-block
**Title:** Discount
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-order-summary-fee-block
**Title:** Fees
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-order-summary-heading-block
**Title:** Heading
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| content | string | Cart totals |  |  |
| lock | object | {"move": false, "remove": false} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-order-summary-shipping-block
**Title:** Shipping
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-cross-sells-block
**Title:** Cart Cross-Sells
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/cart-cross-sells-products-block
**Title:** Cart Cross-Sells Products
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| columns | number | 3 |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "email": true,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout
**Title:** Checkout
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |
| isPreview | boolean | false |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showFormStepNumbers | boolean | false |  |  |

### Supports
```json
{
  "align": [
    "wide"
  ],
  "html": false,
  "multiple": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-actions-block
**Title:** Actions
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| cartPageId | number | 0 |  |  |
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |
| priceSeparator | string | · |  |  |
| showReturnToCart | boolean | true |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-additional-information-block
**Title:** Additional information
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-billing-address-block
**Title:** Billing Address
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-contact-information-block
**Title:** Contact Information
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-express-payment-block
**Title:** Express Checkout
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| buttonBorderRadius | string | 4 |  |  |
| buttonHeight | string | 48 |  |  |
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |
| showButtonStyles | boolean | false |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-fields-block
**Title:** Checkout Fields
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-note-block
**Title:** Order Note
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": false} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-summary-block
**Title:** Order Summary
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-summary-cart-items-block
**Title:** Cart Items
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| disableProductDescriptions | boolean | false |  |  |
| lock | object | {"move": false, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-summary-coupon-form-block
**Title:** Coupon Form
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": false} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-summary-discount-block
**Title:** Discount
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-summary-fee-block
**Title:** Fees
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-summary-shipping-block
**Title:** Shipping
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-summary-subtotal-block
**Title:** Subtotal
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-summary-taxes-block
**Title:** Taxes
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-order-summary-totals-block
**Title:** Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-payment-block
**Title:** Payment Options
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-shipping-address-block
**Title:** Shipping Address
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-shipping-methods-block
**Title:** Shipping Options
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-shipping-method-block
**Title:** Delivery
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-pickup-options-block
**Title:** Pickup Method
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-terms-block
**Title:** Terms and Conditions
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkbox | boolean | false |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| showSeparator | boolean | true |  |  |
| text | string |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/checkout-totals-block
**Title:** Checkout Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkbox | boolean | false |  |  |
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| text | string |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-contents
**Title:** Mini-Cart Contents
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| isPreview | boolean | false |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |
| width | string | 480px |  |  |

### Supports
```json
{
  "__experimentalBorder": {
    "color": true,
    "width": true
  },
  "align": false,
  "color": {
    "background": true,
    "link": true,
    "text": true
  },
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/empty-mini-cart-contents-block
**Title:** Empty Mini-Cart view
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "interactivity": true,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/filled-mini-cart-contents-block
**Title:** Filled Mini-Cart view
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "interactivity": true,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-footer-block
**Title:** Mini-Cart Footer
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "interactivity": true,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-items-block
**Title:** Mini-Cart Items
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-products-table-block
**Title:** Mini-Cart Products Table
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": true} |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "interactivity": true,
  "lock": false,
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-shopping-button-block
**Title:** Mini-Cart Shopping Button
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| lock | object | {"move": false, "remove": false} |  |  |
| metadata | object |  |  |  |
| startShoppingButtonLabel | string |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": false,
  "color": {
    "background": true,
    "text": true
  },
  "html": false,
  "inserter": true,
  "interactivity": {
    "clientNavigation": true
  },
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-cart-button-block
**Title:** Mini-Cart View Cart Button
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| cartButtonLabel | string |  |  |  |
| className | string |  |  |  |
| lock | object | {"move": false, "remove": false} |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": false,
  "color": {
    "background": true,
    "text": true
  },
  "html": false,
  "inserter": true,
  "interactivity": {
    "clientNavigation": true
  },
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-checkout-button-block
**Title:** Mini-Cart Proceed to Checkout Button
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| checkoutButtonLabel | string |  |  |  |
| className | string |  |  |  |
| lock | object | {"move": false, "remove": false} |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": false,
  "color": {
    "background": true,
    "text": true
  },
  "html": false,
  "inserter": true,
  "interactivity": {
    "clientNavigation": true
  },
  "multiple": false,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-title-block
**Title:** Mini-Cart Title
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": false,
  "color": {
    "background": false,
    "text": true
  },
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "lock": false,
  "multiple": false,
  "reusable": false,
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-title-items-counter-block
**Title:** Mini-Cart Title Items Counter
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": false,
  "color": {
    "background": true,
    "text": true
  },
  "html": false,
  "inserter": false,
  "interactivity": true,
  "lock": false,
  "multiple": false,
  "reusable": false,
  "spacing": {
    "padding": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/mini-cart-title-label-block
**Title:** Mini-Cart Title Label
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| label | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": false,
  "color": {
    "background": true,
    "text": true
  },
  "html": false,
  "inserter": false,
  "interactivity": {
    "clientNavigation": true
  },
  "lock": false,
  "multiple": false,
  "reusable": false,
  "spacing": {
    "padding": true
  },
  "typography": {
    "fontSize": true
  }
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-with-options
**Title:** Add to Cart + Options (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| isDescendantOfAddToCartWithOptions | boolean | true |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-with-options-quantity-selector
**Title:** Product Quantity (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-with-options-variation-description
**Title:** Variation Description (Beta)
**Category:** woocommerce
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| borderColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

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
    "gradients": true,
    "link": true
  },
  "dimensions": {
    "minHeight": true
  },
  "html": false,
  "interactivity": true,
  "spacing": {
    "margin": true,
    "padding": true
  },
  "typography": {
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
## woocommerce/add-to-cart-with-options-variation-selector
**Title:** Variation Selector (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-with-options-variation-selector-attribute
**Title:** Variation Selector: Template (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "inserter": false,
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-with-options-variation-selector-attribute-name
**Title:** Variation Selector: Attribute Name (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "align": false,
  "alignWide": false,
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "__experimentalSkipSerialization": true,
    "gradients": true
  },
  "inserter": false,
  "interactivity": true,
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
## woocommerce/add-to-cart-with-options-variation-selector-attribute-options
**Title:** Variation Selector: Attribute Options (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| optionStyle | string |  |  |  |

### Supports
```json
{
  "inserter": false,
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-with-options-grouped-product-selector
**Title:** Grouped Product Selector (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-with-options-grouped-product-item
**Title:** Grouped Product: Template (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "inserter": false,
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-with-options-grouped-product-item-selector
**Title:** Grouped Product: Item Selector (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |

### Supports
```json
{
  "inserter": false,
  "interactivity": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/add-to-cart-with-options-grouped-product-item-label
**Title:** Grouped Product: Item Label (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontFamily | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| layout | object |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
  "color": {
    "__experimentalDefaultControls": {
      "background": true,
      "text": true
    },
    "background": true,
    "gradients": true,
    "text": true
  },
  "html": false,
  "layout": {
    "selfStretch": true
  },
  "spacing": {
    "blockGap": true,
    "margin": true,
    "padding": true
  },
  "typography": {
    "__experimentalDefaultControls": {
      "fontSize": true,
      "fontStyle": true,
      "fontWeight": true
    },
    "__experimentalFontFamily": true,
    "__experimentalFontStyle": true,
    "__experimentalFontWeight": true,
    "__experimentalLetterSpacing": true,
    "__experimentalTextDecoration": true,
    "__experimentalTextTransform": true,
    "fontSize": true,
    "lineHeight": true,
    "textAlign": true
  }
}
```

### Example Markup
_Not generated yet._

---
## core/post-comments
**Title:** 
**Category:** theme
**API Version:** 1
**Origin:** 
**Dynamic:** 

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| backgroundColor | string |  |  |  |
| className | string |  |  |  |
| fontSize | string |  |  |  |
| gradient | string |  |  |  |
| lock | object |  |  |  |
| metadata | object |  |  |  |
| style | object |  |  |  |
| textAlign | string |  |  |  |
| textColor | string |  |  |  |

### Supports
```json
{
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
  "inserter": false,
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