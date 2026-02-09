---
wordpress_version: 6.9.1
plugin_slug: woocommerce
plugin_version: 10.5.0
generated_at_utc: 2026-02-09T13:52:55Z
source_roots: woocommerce: /Users/stephenfeather/Development/wp-block-catalog/artifacts/woocommerce/woocommerce
---

# WordPress Blocks Catalog (6.9.1)

## woocommerce/accordion-group
**Title:** Accordion Group
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| allowedBlocks | array |  |  |  |
| autoclose | boolean | false |  |  |
| iconPosition | string | right |  |  |

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
```html
<!-- wp:woocommerce/accordion-group /-->
```

---
## woocommerce/accordion-header
**Title:** Accordion Header
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| icon | ["string", "boolean"] | plus |  |  |
| iconPosition | string | right |  |  |
| level | number | 3 |  |  |
| levelOptions | array |  |  |  |
| openByDefault | boolean | false |  |  |
| textAlignment | string | left |  |  |
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
```html
<!-- wp:woocommerce/accordion-header /-->
```

---
## woocommerce/accordion-item
**Title:** Accordion
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/accordion-item /-->
```

---
## woocommerce/accordion-panel
**Title:** Accordion Panel
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| allowedBlocks | array |  |  |  |
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
```html
<!-- wp:woocommerce/accordion-panel /-->
```

---
## woocommerce/active-filters
**Title:** Active Filters Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| displayStyle | string | list |  |  |
| headingLevel | number | 3 |  |  |

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
```html
<!-- wp:woocommerce/active-filters {"displayStyle":"list","headingLevel":3} /-->
```

---
## woocommerce/add-to-cart-form
**Title:** Add to Cart with Options
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| quantitySelectorStyle | string | input |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/add-to-cart-form {"quantitySelectorStyle":"input"} /-->
```

---
## woocommerce/add-to-cart-with-options
**Title:** Add to Cart + Options (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendantOfAddToCartWithOptions | boolean | true |  |  |

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/add-to-cart-with-options {"isDescendantOfAddToCartWithOptions":true} /-->
```

---
## woocommerce/add-to-cart-with-options-grouped-product-item
**Title:** Grouped Product: Template (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "inserter": false,
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/add-to-cart-with-options-grouped-product-item /-->
```

---
## woocommerce/add-to-cart-with-options-grouped-product-item-label
**Title:** Grouped Product: Item Label (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/add-to-cart-with-options-grouped-product-item-label /-->
```

---
## woocommerce/add-to-cart-with-options-grouped-product-item-selector
**Title:** Grouped Product: Item Selector (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "inserter": false,
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/add-to-cart-with-options-grouped-product-item-selector /-->
```

---
## woocommerce/add-to-cart-with-options-grouped-product-selector
**Title:** Grouped Product Selector (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/add-to-cart-with-options-grouped-product-selector /-->
```

---
## woocommerce/add-to-cart-with-options-quantity-selector
**Title:** Product Quantity (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/add-to-cart-with-options-quantity-selector /-->
```

---
## woocommerce/add-to-cart-with-options-variation-description
**Title:** Variation Description (Beta)
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/add-to-cart-with-options-variation-description /-->
```

---
## woocommerce/add-to-cart-with-options-variation-selector
**Title:** Variation Selector (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/add-to-cart-with-options-variation-selector /-->
```

---
## woocommerce/add-to-cart-with-options-variation-selector-attribute
**Title:** Variation Selector: Template (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "inserter": false,
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/add-to-cart-with-options-variation-selector-attribute /-->
```

---
## woocommerce/add-to-cart-with-options-variation-selector-attribute-name
**Title:** Variation Selector: Attribute Name (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/add-to-cart-with-options-variation-selector-attribute-name /-->
```

---
## woocommerce/add-to-cart-with-options-variation-selector-attribute-options
**Title:** Variation Selector: Attribute Options (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| optionStyle | string |  |  |  |

### Supports
```json
{
  "inserter": false,
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/add-to-cart-with-options-variation-selector-attribute-options /-->
```

---
## woocommerce/all-products
**Title:** All Products
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alignButtons | boolean |  |  |  |
| columns | number |  |  |  |
| contentVisibility | object |  |  |  |
| isPreview | boolean | false |  |  |
| layoutConfig | array |  |  |  |
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
```html
<!-- wp:woocommerce/all-products {"isPreview":false} /-->
```

---
## woocommerce/all-reviews
**Title:** All Reviews
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/all-reviews /-->
```

---
## woocommerce/attribute-filter
**Title:** Filter by Attribute Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| attributeId | number | 0 |  |  |
| className | string |  |  |  |
| displayStyle | string | list |  |  |
| headingLevel | number | 3 |  |  |
| isPreview | boolean | false |  |  |
| queryType | string | or |  |  |
| selectType | string | multiple |  |  |
| showCounts | boolean | false |  |  |
| showFilterButton | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/attribute-filter {"className":"","attributeId":0,"showCounts":false,"queryType":"or","headingLevel":3,"displayStyle":"list","showFilterButton":false,"selectType":"multiple","isPreview":false} /-->
```

---
## woocommerce/breadcrumbs
**Title:** Store Breadcrumbs
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| contentJustification | string |  |  |  |
| fontSize | string | small |  |  |

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
```html
<!-- wp:woocommerce/breadcrumbs {"fontSize":"small","align":"wide"} /-->
```

---
## woocommerce/cart-accepted-payment-methods-block
**Title:** Accepted Payment Methods
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/cart-accepted-payment-methods-block /-->
```

---
## woocommerce/cart-cross-sells-block
**Title:** Cart Cross-Sells
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/cart-cross-sells-block /-->
```

---
## woocommerce/cart-cross-sells-products-block
**Title:** Cart Cross-Sells Products
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| columns | number | 3 |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-cross-sells-products-block {"columns":3,"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-express-payment-block
**Title:** Express Checkout
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| buttonBorderRadius | string | 4 |  |  |
| buttonHeight | string | 48 |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
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
```html
<!-- wp:woocommerce/cart-express-payment-block {"showButtonStyles":false,"buttonHeight":"48","buttonBorderRadius":"4","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-items-block
**Title:** Cart Items
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-items-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-line-items-block
**Title:** Cart Line Items
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-line-items-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-link
**Title:** Cart Link
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| cartIcon | string | cart |  |  |
| content | string |  |  |  |
| isPreview | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/cart-link {"isPreview":true,"cartIcon":"cart","content":"Cart"} /-->
```

---
## woocommerce/cart-order-summary-block
**Title:** Order Summary
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-order-summary-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-order-summary-coupon-form-block
**Title:** Coupon Form
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": false} |  |  |

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
```html
<!-- wp:woocommerce/cart-order-summary-coupon-form-block {"className":"","lock":{"remove":false,"move":false}} /-->
```

---
## woocommerce/cart-order-summary-discount-block
**Title:** Discount
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-order-summary-discount-block {"className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-order-summary-fee-block
**Title:** Fees
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-order-summary-fee-block {"className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-order-summary-heading-block
**Title:** Heading
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| content | string | Cart totals |  |  |
| lock | object | {"move": false, "remove": false} |  |  |

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
```html
<!-- wp:woocommerce/cart-order-summary-heading-block {"className":"","content":"Cart totals","lock":{"remove":false,"move":false}} /-->
```

---
## woocommerce/cart-order-summary-shipping-block
**Title:** Shipping
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-order-summary-shipping-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-order-summary-subtotal-block
**Title:** Subtotal
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-order-summary-subtotal-block {"className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-order-summary-taxes-block
**Title:** Taxes
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-order-summary-taxes-block {"className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/cart-order-summary-totals-block
**Title:** Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/cart-order-summary-totals-block {"className":"","lock":{"remove":true,"move":false}} /-->
```

---
## woocommerce/cart-totals-block
**Title:** Cart Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkbox | boolean | false |  |  |
| lock | object | {"remove": true} |  |  |
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
```html
<!-- wp:woocommerce/cart-totals-block {"checkbox":false,"lock":{"remove":true}} /-->
```

---
## woocommerce/catalog-sorting
**Title:** Catalog Sorting
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| fontSize | string | small |  |  |
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
```html
<!-- wp:woocommerce/catalog-sorting {"fontSize":"small","useLabel":false} /-->
```

---
## woocommerce/category-description
**Title:** Product Category Description
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

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
```html
<!-- wp:woocommerce/category-description /-->
```

---
## woocommerce/category-title
**Title:** Product Category Title
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isLink | boolean | false |  |  |
| level | number | 2 |  |  |
| linkTarget | string | _self |  |  |
| rel | string |  |  |  |
| textAlign | string |  |  |  |

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
```html
<!-- wp:woocommerce/category-title {"isLink":false,"level":2,"linkTarget":"_self","rel":""} /-->
```

---
## woocommerce/checkout
**Title:** Checkout
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/checkout {"isPreview":true} /-->
```

---
## woocommerce/checkout-actions-block
**Title:** Actions
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| cartPageId | number | 0 |  |  |
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
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
```html
<!-- wp:woocommerce/checkout-actions-block {"lock":{"remove":true,"move":true},"cartPageId":0,"showReturnToCart":true,"className":"","priceSeparator":"·"} /-->
```

---
## woocommerce/checkout-additional-information-block
**Title:** Additional information
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-additional-information-block {"className":"","lock":{"remove":true,"move":false}} /-->
```

---
## woocommerce/checkout-billing-address-block
**Title:** Billing Address
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-billing-address-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-contact-information-block
**Title:** Contact Information
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-contact-information-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-express-payment-block
**Title:** Express Checkout
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| buttonBorderRadius | string | 4 |  |  |
| buttonHeight | string | 48 |  |  |
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
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
```html
<!-- wp:woocommerce/checkout-express-payment-block {"showButtonStyles":false,"buttonHeight":"48","buttonBorderRadius":"4","className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-fields-block
**Title:** Checkout Fields
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-fields-block {"className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-order-note-block
**Title:** Order Note
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": false} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-note-block {"className":"","lock":{"remove":false,"move":true}} /-->
```

---
## woocommerce/checkout-order-summary-block
**Title:** Order Summary
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-summary-block {"lock":{"remove":true}} /-->
```

---
## woocommerce/checkout-order-summary-cart-items-block
**Title:** Cart Items
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| disableProductDescriptions | boolean | false |  |  |
| lock | object | {"move": false, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-summary-cart-items-block {"className":"","disableProductDescriptions":false,"lock":{"remove":true,"move":false}} /-->
```

---
## woocommerce/checkout-order-summary-coupon-form-block
**Title:** Coupon Form
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": false} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-summary-coupon-form-block {"className":"","lock":{"remove":false,"move":false}} /-->
```

---
## woocommerce/checkout-order-summary-discount-block
**Title:** Discount
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-summary-discount-block {"className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-order-summary-fee-block
**Title:** Fees
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-summary-fee-block {"className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-order-summary-shipping-block
**Title:** Shipping
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-summary-shipping-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-order-summary-subtotal-block
**Title:** Subtotal
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-summary-subtotal-block {"className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-order-summary-taxes-block
**Title:** Taxes
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-summary-taxes-block {"className":"","lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-order-summary-totals-block
**Title:** Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| lock | object | {"move": false, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-order-summary-totals-block {"className":"","lock":{"remove":true,"move":false}} /-->
```

---
## woocommerce/checkout-payment-block
**Title:** Payment Options
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-payment-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-pickup-options-block
**Title:** Pickup Method
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-pickup-options-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-shipping-address-block
**Title:** Shipping Address
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-shipping-address-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-shipping-method-block
**Title:** Delivery
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-shipping-method-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-shipping-methods-block
**Title:** Shipping Options
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/checkout-shipping-methods-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/checkout-terms-block
**Title:** Terms and Conditions
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkbox | boolean | false |  |  |
| className | string |  |  |  |
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
```html
<!-- wp:woocommerce/checkout-terms-block {"className":"","checkbox":false,"showSeparator":true} /-->
```

---
## woocommerce/checkout-totals-block
**Title:** Checkout Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkbox | boolean | false |  |  |
| className | string |  |  |  |
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
```html
<!-- wp:woocommerce/checkout-totals-block {"className":"","checkbox":false} /-->
```

---
## woocommerce/classic-shortcode
**Title:** Classic Shortcode
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
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
```html
<!-- wp:woocommerce/classic-shortcode {"shortcode":"cart","align":"wide"} /-->
```

---
## woocommerce/coming-soon
**Title:** Coming Soon
**Category:** woocommerce
**API Version:** 
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| color | string |  |  |  |
| comingSoonPatternId | string |  |  |  |
| storeOnly | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/coming-soon {"storeOnly":false,"comingSoonPatternId":""} /-->
```

---
## woocommerce/conditional
**Title:** Conditional
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| mustMatch | array | [] |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/coupon-code
**Title:** Coupon Code
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| couponCode | string |  |  |  |

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
```html
<!-- wp:woocommerce/coupon-code {"couponCode":""} /-->
```

---
## woocommerce/customer-account
**Title:** Customer account
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| displayStyle | string | icon_and_text |  |  |
| iconClass | string | icon |  |  |
| iconStyle | string | default |  |  |

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
```html
<!-- wp:woocommerce/customer-account {"displayStyle":"icon_and_text","iconStyle":"default","iconClass":"icon"} /-->
```

---
## woocommerce/email-content
**Title:** Email Content
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| emailType | string |  |  |  |
| postId | integer |  |  |  |

### Supports
```json
{
  "email": true,
  "inserter": false
}
```

### Example Markup
```html
<!-- wp:woocommerce/email-content /-->
```

---
## woocommerce/empty-cart-block
**Title:** Empty Cart
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/empty-cart-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/empty-mini-cart-contents-block
**Title:** Empty Mini-Cart view
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/empty-mini-cart-contents-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/featured-category
**Title:** Featured Category
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alt | string |  |  |  |
| categoryId | number |  |  |  |
| contentAlign | string | center |  |  |
| dimRatio | number | 50 |  |  |
| focalPoint | object | {"x": 0.5, "y": 0.5} |  |  |
| hasParallax | boolean | false |  |  |
| imageFit | string | none |  |  |
| isRepeated | boolean | false |  |  |
| linkText | string | Shop now |  |  |
| mediaId | number | 0 |  |  |
| mediaSrc | string |  |  |  |
| minHeight | number | 500 |  |  |
| overlayColor | string | #000000 |  |  |
| overlayGradient | string |  |  |  |
| previewCategory | object |  |  |  |

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
```html
<!-- wp:woocommerce/featured-category {"alt":"","contentAlign":"center","dimRatio":50,"focalPoint":{"x":0.5,"y":0.5},"imageFit":"none","hasParallax":false,"isRepeated":false,"mediaId":0,"mediaSrc":"","minHeight":500,"linkText":"Shop now","overlayColor":"#000000","previewCategory":null} /-->
```

---
## woocommerce/featured-product
**Title:** Featured Product
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alt | string |  |  |  |
| contentAlign | string | center |  |  |
| dimRatio | number | 50 |  |  |
| focalPoint | object | {"x": 0.5, "y": 0.5} |  |  |
| hasParallax | boolean | false |  |  |
| imageFit | string | none |  |  |
| isRepeated | boolean | false |  |  |
| linkText | string | Shop now |  |  |
| mediaId | number | 0 |  |  |
| mediaSrc | string |  |  |  |
| minHeight | number | 500 |  |  |
| overlayColor | string | #000000 |  |  |
| overlayGradient | string |  |  |  |
| previewProduct | object |  |  |  |
| productId | number |  |  |  |

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
```html
<!-- wp:woocommerce/featured-product {"alt":"","contentAlign":"center","dimRatio":50,"focalPoint":{"x":0.5,"y":0.5},"imageFit":"none","hasParallax":false,"isRepeated":false,"mediaId":0,"mediaSrc":"","minHeight":500,"linkText":"Shop now","overlayColor":"#000000","previewProduct":null} /-->
```

---
## woocommerce/filled-cart-block
**Title:** Filled Cart
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/filled-cart-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/filled-mini-cart-contents-block
**Title:** Filled Mini-Cart view
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/filled-mini-cart-contents-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/filter-wrapper
**Title:** Filter Block
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| filterType | string |  |  |  |
| heading | string |  |  |  |

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
```html
<!-- wp:woocommerce/filter-wrapper /-->
```

---
## woocommerce/handpicked-products
**Title:** Hand-picked Products
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| alignButtons | boolean | false |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/handpicked-products {"columns":3,"contentVisibility":{"image":true,"title":true,"price":true,"rating":true,"button":true},"orderby":"date","products":[],"alignButtons":false,"isPreview":false} /-->
```

---
## woocommerce/mini-cart
**Title:** Mini-Cart
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| addToCartBehaviour | string | none |  |  |
| cartAndCheckoutRenderStyle | string | hidden |  |  |
| hasHiddenPrice | boolean | true |  |  |
| iconColor | object |  |  |  |
| iconColorValue | string |  |  |  |
| isPreview | boolean | false |  |  |
| miniCartIcon | string | cart |  |  |
| onCartClickBehaviour | string | open_drawer |  |  |
| priceColor | object |  |  |  |
| priceColorValue | string |  |  |  |
| productCountColor | object |  |  |  |
| productCountColorValue | string |  |  |  |
| productCountVisibility | string | greater_than_zero |  |  |

### Supports
```json
{
  "html": false,
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
```html
<!-- wp:woocommerce/mini-cart {"isPreview":true,"className":"wc-block-mini-cart\u002d\u002dpreview"} /-->
```

---
## woocommerce/mini-cart-cart-button-block
**Title:** Mini-Cart View Cart Button
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| cartButtonLabel | string |  |  |  |
| lock | object | {"move": false, "remove": false} |  |  |

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
```html
<!-- wp:woocommerce/mini-cart-cart-button-block {"lock":{"remove":false,"move":false},"cartButtonLabel":""} /-->
```

---
## woocommerce/mini-cart-checkout-button-block
**Title:** Mini-Cart Proceed to Checkout Button
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkoutButtonLabel | string |  |  |  |
| lock | object | {"move": false, "remove": false} |  |  |

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
```html
<!-- wp:woocommerce/mini-cart-checkout-button-block {"lock":{"remove":false,"move":false},"checkoutButtonLabel":""} /-->
```

---
## woocommerce/mini-cart-contents
**Title:** Mini-Cart Contents
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isPreview | boolean | false |  |  |
| lock | object | {"move": true, "remove": true} |  |  |
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
```html
<!-- wp:woocommerce/mini-cart-contents {"isPreview":false,"lock":{"remove":true,"move":true},"width":"480px"} /-->
```

---
## woocommerce/mini-cart-footer-block
**Title:** Mini-Cart Footer
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/mini-cart-footer-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/mini-cart-items-block
**Title:** Mini-Cart Items
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/mini-cart-items-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/mini-cart-products-table-block
**Title:** Mini-Cart Products Table
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": false, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/mini-cart-products-table-block {"lock":{"remove":true,"move":false}} /-->
```

---
## woocommerce/mini-cart-shopping-button-block
**Title:** Mini-Cart Shopping Button
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": false, "remove": false} |  |  |
| startShoppingButtonLabel | string |  |  |  |

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
```html
<!-- wp:woocommerce/mini-cart-shopping-button-block {"lock":{"remove":false,"move":false},"startShoppingButtonLabel":""} /-->
```

---
## woocommerce/mini-cart-title-block
**Title:** Mini-Cart Title
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/mini-cart-title-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/mini-cart-title-items-counter-block
**Title:** Mini-Cart Title Items Counter
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/mini-cart-title-items-counter-block /-->
```

---
## woocommerce/mini-cart-title-label-block
**Title:** Mini-Cart Title Label
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

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
```html
<!-- wp:woocommerce/mini-cart-title-label-block {"label":""} /-->
```

---
## woocommerce/order-confirmation-additional-fields
**Title:** Additional Field List
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-additional-fields {"align":"wide","className":""} /-->
```

---
## woocommerce/order-confirmation-additional-fields-wrapper
**Title:** Additional Fields
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| heading | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-additional-fields-wrapper /-->
```

---
## woocommerce/order-confirmation-additional-information
**Title:** Additional Information
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-additional-information {"align":"wide","className":""} /-->
```

---
## woocommerce/order-confirmation-billing-address
**Title:** Billing Address
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-billing-address {"align":"wide"} /-->
```

---
## woocommerce/order-confirmation-billing-wrapper
**Title:** Billing Address Section
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| heading | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-billing-wrapper /-->
```

---
## woocommerce/order-confirmation-create-account
**Title:** Account Creation
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |
| customerEmail | string |  |  |  |
| hasDarkControls | boolean | false |  |  |
| lock | object | {"remove": true} |  |  |
| nonceToken | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-create-account {"customerEmail":"","nonceToken":"","align":"wide","className":"","hasDarkControls":false,"lock":{"remove":true}} /-->
```

---
## woocommerce/order-confirmation-downloads
**Title:** Order Downloads
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-downloads {"align":"wide","className":""} /-->
```

---
## woocommerce/order-confirmation-downloads-wrapper
**Title:** Downloads Section
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| heading | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-downloads-wrapper /-->
```

---
## woocommerce/order-confirmation-shipping-address
**Title:** Shipping Address
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-shipping-address {"align":"wide"} /-->
```

---
## woocommerce/order-confirmation-shipping-wrapper
**Title:** Shipping Address Section
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| heading | string | Shipping |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-shipping-wrapper {"heading":"Shipping"} /-->
```

---
## woocommerce/order-confirmation-status
**Title:** Order Status
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-status {"align":"wide","className":""} /-->
```

---
## woocommerce/order-confirmation-summary
**Title:** Order Summary
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-summary {"align":"wide","className":""} /-->
```

---
## woocommerce/order-confirmation-totals
**Title:** Order Totals
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| className | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-totals {"align":"wide","className":""} /-->
```

---
## woocommerce/order-confirmation-totals-wrapper
**Title:** Order Totals Section
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| heading | string |  |  |  |

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
```html
<!-- wp:woocommerce/order-confirmation-totals-wrapper /-->
```

---
## woocommerce/page-content-wrapper
**Title:** WooCommerce Page
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
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
```html
<!-- wp:woocommerce/page-content-wrapper {"page":""} /-->
```

---
## woocommerce/payment-method-icons
**Title:** Payment Method Icons
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| numberOfIcons | number | 0 |  |  |

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
```html
<!-- wp:woocommerce/payment-method-icons {"numberOfIcons":0} /-->
```

---
## woocommerce/price-filter
**Title:** Filter by Price Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| headingLevel | number | 3 |  |  |
| inlineInput | boolean | false |  |  |
| showFilterButton | boolean | false |  |  |
| showInputFields | boolean | true |  |  |

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
```html
<!-- wp:woocommerce/price-filter {"className":"","showInputFields":true,"inlineInput":false,"showFilterButton":false,"headingLevel":3} /-->
```

---
## woocommerce/proceed-to-checkout-block
**Title:** Proceed to Checkout
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| lock | object | {"move": true, "remove": true} |  |  |

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
```html
<!-- wp:woocommerce/proceed-to-checkout-block {"lock":{"remove":true,"move":true}} /-->
```

---
## woocommerce/product-attributes-field
**Title:** Product attributes
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-attributes-field
**Title:** Product attributes
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-average-rating
**Title:** Product Average Rating (Beta)
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

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
```html
<!-- wp:woocommerce/product-average-rating /-->
```

---
## woocommerce/product-best-sellers
**Title:** Best Selling Products
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| editMode | boolean | true |  |  |
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/product-best-sellers {"columns":3,"rows":3,"alignButtons":false,"contentVisibility":{"image":true,"title":true,"price":true,"rating":true,"button":true},"categories":[],"catOperator":"any","isPreview":false,"editMode":true,"orderby":"popularity"} /-->
```

---
## woocommerce/product-button
**Title:** Add to Cart Button
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| productId | number | 0 |  |  |
| textAlign | string |  |  |  |
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
```html
<!-- wp:woocommerce/product-button {"productId":0,"textAlign":"","isDescendentOfSingleProductBlock":false,"isDescendentOfQueryLoop":false} /-->
```

---
## woocommerce/product-catalog-visibility-field
**Title:** Product catalog visibility
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |
| visibility | string | visible |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-catalog-visibility-field
**Title:** Product catalog visibility
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |
| visibility | string | visible |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-categories
**Title:** Product Categories List
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| hasCount | boolean | true |  |  |
| hasEmpty | boolean | false |  |  |
| hasImage | boolean | false |  |  |
| isDropdown | boolean | false |  |  |
| isHierarchical | boolean | true |  |  |
| showChildrenOnly | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/product-categories {"hasCount":true,"hasImage":false} /-->
```

---
## woocommerce/product-category
**Title:** Products by Category
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| editMode | boolean | true |  |  |
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/product-category {"columns":3,"rows":3,"alignButtons":false,"contentVisibility":{"image":true,"title":true,"price":true,"rating":true,"button":true},"categories":[],"catOperator":"any","isPreview":false,"editMode":true,"orderby":"date"} /-->
```

---
## woocommerce/product-checkbox-field
**Title:** Product checkbox control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkedValue | string |  |  |  |
| label | string |  |  |  |
| property | string |  |  |  |
| title | string |  |  |  |
| tooltip | string |  |  |  |
| uncheckedValue | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-checkbox-field
**Title:** Product checkbox control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkedValue | string |  |  |  |
| label | string |  |  |  |
| property | string |  |  |  |
| title | string |  |  |  |
| tooltip | string |  |  |  |
| uncheckedValue | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-collapsible
**Title:** Collapsible
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| initialCollapsed | boolean |  |  |  |
| persistRender | boolean |  |  |  |
| toggleText | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-collapsible
**Title:** Collapsible
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| initialCollapsed | boolean |  |  |  |
| persistRender | boolean |  |  |  |
| toggleText | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-collection
**Title:** Product Collection
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| __privatePreviewState | object |  |  |  |
| collection | string |  |  |  |
| convertedFromProducts | boolean | false |  |  |
| dimensions | object |  |  |  |
| displayLayout | object |  |  |  |
| forcePageReload | boolean | false |  |  |
| hideControls | array | [] |  |  |
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
```html
<!-- wp:woocommerce/product-collection {"convertedFromProducts":false,"hideControls":[],"forcePageReload":false} /-->
```

---
## woocommerce/product-collection-no-results
**Title:** No results
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-collection-no-results /-->
```

---
## woocommerce/product-custom-fields
**Title:** Product custom fields control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-custom-fields
**Title:** Product custom fields control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-custom-fields-toggle-field
**Title:** Product custom fields toggle control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-custom-fields-toggle-field
**Title:** Product custom fields toggle control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-description
**Title:** Product Description
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-description /-->
```

---
## woocommerce/product-description-field
**Title:** Product description
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| __contentEditable | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": true,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-description-field
**Title:** Product description
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| __contentEditable | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": true,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-details
**Title:** Product Details
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |
| hideTabTitle | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/product-details {"align":"wide","hideTabTitle":false} /-->
```

---
## woocommerce/product-details-section-description
**Title:** Product details section description
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-downloads-field
**Title:** Product downloads
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-downloads-field
**Title:** Product downloads
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-filter-active
**Title:** Active Filters
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-filter-active /-->
```

---
## woocommerce/product-filter-attribute
**Title:** Attribute Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| attributeId | number | 0 |  |  |
| displayStyle | string | woocommerce/product-filter-checkbox-list |  |  |
| hideEmpty | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| queryType | string | or |  |  |
| selectType | string | multiple |  |  |
| showCounts | boolean | false |  |  |
| sortOrder | string | count-desc |  |  |

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
```html
<!-- wp:woocommerce/product-filter-attribute {"isPreview":true} /-->
```

---
## woocommerce/product-filter-checkbox-list
**Title:** List
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| customLabelElement | string |  |  |  |
| customOptionElement | string |  |  |  |
| customOptionElementBorder | string |  |  |  |
| customOptionElementSelected | string |  |  |  |
| labelElement | string |  |  |  |
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
```html
<!-- wp:woocommerce/product-filter-checkbox-list {"optionElementBorder":"","customOptionElementBorder":"","optionElementSelected":"","customOptionElementSelected":"","optionElement":"","customOptionElement":"","labelElement":"","customLabelElement":""} /-->
```

---
## woocommerce/product-filter-chips
**Title:** Chips
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| chipBackground | string |  |  |  |
| chipBorder | string |  |  |  |
| chipText | string |  |  |  |
| customChipBackground | string |  |  |  |
| customChipBorder | string |  |  |  |
| customChipText | string |  |  |  |
| customSelectedChipBackground | string |  |  |  |
| customSelectedChipBorder | string |  |  |  |
| customSelectedChipText | string |  |  |  |
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
```html
<!-- wp:woocommerce/product-filter-chips /-->
```

---
## woocommerce/product-filter-clear-button
**Title:** Clear filters
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "inserter": true,
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/product-filter-clear-button /-->
```

---
## woocommerce/product-filter-price
**Title:** Price Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "html": false,
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/product-filter-price /-->
```

---
## woocommerce/product-filter-price-slider
**Title:** Price Slider
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| customSlider | string |  |  |  |
| customSliderHandle | string |  |  |  |
| customSliderHandleBorder | string |  |  |  |
| inlineInput | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/product-filter-price-slider {"showInputFields":true,"inlineInput":false,"sliderHandle":"","customSliderHandle":"","sliderHandleBorder":"","customSliderHandleBorder":"","slider":"","customSlider":""} /-->
```

---
## woocommerce/product-filter-rating
**Title:** Rating Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| isPreview | boolean | false |  |  |
| minRating | string | 0 |  |  |
| showCounts | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/product-filter-rating {"className":"","showCounts":false,"minRating":"0","isPreview":false} /-->
```

---
## woocommerce/product-filter-removable-chips
**Title:** Chips
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| chipBackground | string |  |  |  |
| chipBorder | string |  |  |  |
| chipText | string |  |  |  |
| customChipBackground | string |  |  |  |
| customChipBorder | string |  |  |  |
| customChipText | string |  |  |  |

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
```html
<!-- wp:woocommerce/product-filter-removable-chips /-->
```

---
## woocommerce/product-filter-status
**Title:** Status Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| displayStyle | string | woocommerce/product-filter-checkbox-list |  |  |
| hideEmpty | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| showCounts | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/product-filter-status {"isPreview":true} /-->
```

---
## woocommerce/product-filter-taxonomy
**Title:** Taxonomy Filter
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| displayStyle | string | woocommerce/product-filter-checkbox-list |  |  |
| hideEmpty | boolean | true |  |  |
| isPreview | boolean | false |  |  |
| showCounts | boolean | false |  |  |
| sortOrder | string | count-desc |  |  |
| taxonomy | string | product_cat |  |  |

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
```html
<!-- wp:woocommerce/product-filter-taxonomy {"isPreview":true} /-->
```

---
## woocommerce/product-filters
**Title:** Product Filters
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isPreview | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/product-filters {"isPreview":true} /-->
```

---
## woocommerce/product-gallery
**Title:** Product Gallery
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| fullScreenOnClick | boolean | true |  |  |
| hoverZoom | boolean | true |  |  |

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
```html
<!-- wp:woocommerce/product-gallery /-->
```

---
## woocommerce/product-gallery-large-image
**Title:** Viewer
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

### Supports
```json
{
  "interactivity": true
}
```

### Example Markup
```html
<!-- wp:woocommerce/product-gallery-large-image /-->
```

---
## woocommerce/product-gallery-large-image-next-previous
**Title:** Next/Previous Buttons
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/product-gallery-large-image-next-previous /-->
```

---
## woocommerce/product-gallery-thumbnails
**Title:** Thumbnails
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| activeThumbnailStyle | string | overlay |  |  |
| aspectRatio | string | 1 |  |  |
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
```html
<!-- wp:woocommerce/product-gallery-thumbnails {"thumbnailSize":"25%","aspectRatio":"1","activeThumbnailStyle":"overlay"} /-->
```

---
## woocommerce/product-has-variations-notice
**Title:** Notice
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| buttonText | string |  |  |  |
| content | string |  |  |  |
| title | string |  |  |  |
| type | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-has-variations-notice
**Title:** Notice
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| buttonText | string |  |  |  |
| content | string |  |  |  |
| title | string |  |  |  |
| type | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-image
**Title:** Product Image
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| aspectRatio | string |  |  |  |
| height | string |  |  |  |
| imageSizing | string | single |  |  |
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| productId | number | 0 |  |  |
| saleBadgeAlign | string | right |  |  |
| scale | string | cover |  |  |
| showProductLink | boolean | true |  |  |
| showSaleBadge | boolean | true |  |  |
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
```html
<!-- wp:woocommerce/product-image {"showProductLink":true,"showSaleBadge":true,"saleBadgeAlign":"right","imageSizing":"single","productId":0,"isDescendentOfQueryLoop":false,"isDescendentOfSingleProductBlock":false,"scale":"cover"} /-->
```

---
## woocommerce/product-image-gallery
**Title:** Product Image Gallery
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/product-image-gallery /-->
```

---
## woocommerce/product-images-field
**Title:** Product images
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| images | array | [] |  |  |
| mediaId | number |  |  |  |
| multiple | boolean | true |  |  |
| property | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-images-field
**Title:** Product images
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| images | array | [] |  |  |
| mediaId | number |  |  |  |
| multiple | boolean | true |  |  |
| property | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-inventory-email-field
**Title:** Stock level threshold
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-inventory-email-field
**Title:** Stock level threshold
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-inventory-quantity-field
**Title:** Product inventory quantity available
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-inventory-quantity-field
**Title:** Product inventory quantity available
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-linked-list-field
**Title:** Linked product list
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| emptyState | object | {} |  |  |
| property | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-linked-list-field
**Title:** Linked product list
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| emptyState | object | {} |  |  |
| property | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-list-field
**Title:** Product list
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| property | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-list-field
**Title:** Product list
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| property | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-meta
**Title:** Product Meta
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/product-meta /-->
```

---
## woocommerce/product-name-field
**Title:** Product name
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| autoFocus | boolean | false |  |  |
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-name-field
**Title:** Product name
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| autoFocus | boolean | false |  |  |
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
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
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| editMode | boolean | true |  |  |
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/product-new {"columns":3,"rows":3,"alignButtons":false,"contentVisibility":{"image":true,"title":true,"price":true,"rating":true,"button":true},"categories":[],"catOperator":"any","isPreview":false,"editMode":true,"orderby":"date"} /-->
```

---
## woocommerce/product-notice-field
**Title:** Product notice field
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| message | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-notice-field
**Title:** Product notice field
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| message | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-number-field
**Title:** Product number control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| help | string |  |  |  |
| label | string |  |  |  |
| max | number |  |  |  |
| min | number |  |  |  |
| placeholder | string |  |  |  |
| property | string |  |  |  |
| required | boolean | false |  |  |
| step | number | 1 |  |  |
| suffix | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-number-field
**Title:** Product number control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| help | string |  |  |  |
| label | string |  |  |  |
| max | number |  |  |  |
| min | number |  |  |  |
| placeholder | string |  |  |  |
| property | string |  |  |  |
| required | boolean | false |  |  |
| step | number | 1 |  |  |
| suffix | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-on-sale
**Title:** On Sale Products
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/product-on-sale {"columns":3,"rows":3,"alignButtons":false,"categories":[],"catOperator":"any","contentVisibility":{"image":true,"title":true,"price":true,"rating":true,"button":true},"isPreview":false,"orderby":"date"} /-->
```

---
## woocommerce/product-password-field
**Title:** Product password
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-password-field
**Title:** Product password
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-price
**Title:** Product Price
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| productId | number | 0 |  |  |
| textAlign | string |  |  |  |

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
```html
<!-- wp:woocommerce/product-price {"productId":0,"isDescendentOfQueryLoop":false,"textAlign":"","isDescendentOfSingleProductTemplate":false,"isDescendentOfSingleProductBlock":false} /-->
```

---
## woocommerce/product-pricing-field
**Title:** Product pricing
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| help | string |  |  |  |
| label | string |  |  |  |
| property | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-pricing-field
**Title:** Product pricing
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| help | string |  |  |  |
| label | string |  |  |  |
| property | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-radio-field
**Title:** Product radio control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| description | string |  |  |  |
| disabled | boolean | false |  |  |
| options | array | [] |  |  |
| property | string |  |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-radio-field
**Title:** Product radio control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| description | string |  |  |  |
| disabled | boolean | false |  |  |
| options | array | [] |  |  |
| property | string |  |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-rating
**Title:** Product Rating
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| productId | number | 0 |  |  |
| textAlign | string |  |  |  |

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
```html
<!-- wp:woocommerce/product-rating {"productId":0,"isDescendentOfQueryLoop":false,"textAlign":"","isDescendentOfSingleProductBlock":false,"isDescendentOfSingleProductTemplate":false} /-->
```

---
## woocommerce/product-rating-counter
**Title:** Product Rating Counter
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| productId | number | 0 |  |  |
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
```html
<!-- wp:woocommerce/product-rating-counter {"productId":0,"isDescendentOfQueryLoop":false,"textAlign":"","isDescendentOfSingleProductBlock":false,"isDescendentOfSingleProductTemplate":false} /-->
```

---
## woocommerce/product-rating-stars
**Title:** Product Rating Stars
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| productId | number | 0 |  |  |
| textAlign | string |  |  |  |

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
```html
<!-- wp:woocommerce/product-rating-stars {"productId":0,"isDescendentOfQueryLoop":false,"textAlign":"","isDescendentOfSingleProductBlock":false,"isDescendentOfSingleProductTemplate":false} /-->
```

---
## woocommerce/product-regular-price-field
**Title:** Product regular price
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean | false |  |  |
| help | string |  |  |  |
| isRequired | boolean | false |  |  |
| label | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-regular-price-field
**Title:** Product regular price
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean | false |  |  |
| help | string |  |  |  |
| isRequired | boolean | false |  |  |
| label | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-results-count
**Title:** Product Results Count
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/product-results-count /-->
```

---
## woocommerce/product-review-author-name
**Title:** Review Author Name
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-review-author-name {"isLink":true,"linkTarget":"_self"} /-->
```

---
## woocommerce/product-review-content
**Title:** Review Content
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-review-content /-->
```

---
## woocommerce/product-review-date
**Title:** Review Date
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-review-date {"isLink":true} /-->
```

---
## woocommerce/product-review-form
**Title:** Reviews Form
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-review-form {"textAlign":"center"} /-->
```

---
## woocommerce/product-review-rating
**Title:** Review Rating
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| textAlign | string |  |  |  |

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
```html
<!-- wp:woocommerce/product-review-rating /-->
```

---
## woocommerce/product-review-template
**Title:** Reviews Template
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-review-template /-->
```

---
## woocommerce/product-reviews
**Title:** Product Reviews
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-reviews {"tagName":"div"} /-->
```

---
## woocommerce/product-reviews-pagination
**Title:** Reviews Pagination
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-reviews-pagination {"paginationArrow":"none"} /-->
```

---
## woocommerce/product-reviews-pagination-next
**Title:** Reviews Next Page
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-reviews-pagination-next /-->
```

---
## woocommerce/product-reviews-pagination-numbers
**Title:** Reviews Page Numbers
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-reviews-pagination-numbers /-->
```

---
## woocommerce/product-reviews-pagination-previous
**Title:** Reviews Previous Page
**Category:** woocommerce
**API Version:** 3
**Origin:** external
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
```html
<!-- wp:woocommerce/product-reviews-pagination-previous /-->
```

---
## woocommerce/product-reviews-title
**Title:** Reviews Title
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| level | number | 2 |  |  |
| levelOptions | array |  |  |  |
| showProductTitle | boolean | true |  |  |
| showReviewsCount | boolean | true |  |  |
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
```html
<!-- wp:woocommerce/product-reviews-title {"showProductTitle":true,"showReviewsCount":true,"level":2} /-->
```

---
## woocommerce/product-sale-badge
**Title:** On-Sale Badge
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| productId | number | 0 |  |  |

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
```html
<!-- wp:woocommerce/product-sale-badge /-->
```

---
## woocommerce/product-sale-price-field
**Title:** Product sale price
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean | false |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-sale-price-field
**Title:** Product sale price
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean | false |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-schedule-sale-fields
**Title:** Product schedule sale fields
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-schedule-sale-fields
**Title:** Product schedule sale fields
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-section
**Title:** Product section
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| blockGap | string | unit-20 |  |  |
| description | string |  |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-section
**Title:** Product section
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| blockGap | string | unit-20 |  |  |
| description | string |  |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-section-description
**Title:** Product section description
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-section-description
**Title:** Product section description
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-select-field
**Title:** Product select field
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean |  |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| multiple | boolean | false |  |  |
| options | array | [] |  |  |
| property | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-select-field
**Title:** Product select field
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean |  |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| multiple | boolean | false |  |  |
| options | array | [] |  |  |
| property | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-shipping-class-field
**Title:** Product shipping class field
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean | false |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-shipping-class-field
**Title:** Product shipping class field
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean | false |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-shipping-dimensions-fields
**Title:** Product shipping dimensions fields
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| __contentEditable | string |  |  |  |
| disabled | boolean | false |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-shipping-dimensions-fields
**Title:** Product shipping dimensions fields
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| __contentEditable | string |  |  |  |
| disabled | boolean | false |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-single-variation-notice
**Title:** Notice
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  |  |  |
| isDismissible | boolean |  |  |  |
| title | string |  |  |  |
| type | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": true,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-single-variation-notice
**Title:** Notice
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  |  |  |
| isDismissible | boolean |  |  |  |
| title | string |  |  |  |
| type | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": true,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-sku
**Title:** Product SKU
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendantOfAllProducts | boolean | false |  |  |
| prefix | string | SKU: |  |  |
| productId | number | 0 |  |  |
| showProductSelector | boolean | false |  |  |
| suffix | string |  |  |  |

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
```html
<!-- wp:woocommerce/product-sku {"productId":0,"isDescendantOfAllProducts":false,"showProductSelector":false,"prefix":"SKU:","suffix":""} /-->
```

---
## woocommerce/product-sku-field
**Title:** Product text control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean | false |  |  |
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-sku-field
**Title:** Product text control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| disabled | boolean | false |  |  |
| name | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-specifications
**Title:** Product Specifications
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| showAttributes | boolean | true |  |  |
| showDimensions | boolean | true |  |  |
| showWeight | boolean | true |  |  |

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
```html
<!-- wp:woocommerce/product-specifications {"showWeight":true,"showDimensions":true,"showAttributes":true} /-->
```

---
## woocommerce/product-stock-indicator
**Title:** Product Stock Indicator
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendantOfAllProducts | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/product-stock-indicator {"isDescendantOfAllProducts":false} /-->
```

---
## woocommerce/product-subsection
**Title:** Product subsection
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| blockGap | string | unit-20 |  |  |
| description | string |  |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-subsection
**Title:** Product subsection
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| blockGap | string | unit-20 |  |  |
| description | string |  |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-subsection-description
**Title:** Product subsection description
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-subsection-description
**Title:** Product subsection description
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| content | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-summary
**Title:** Product Summary
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isDescendantOfAllProducts | boolean | false |  |  |
| isDescendentOfQueryLoop | boolean | false |  |  |
| isDescendentOfSingleProductBlock | boolean | false |  |  |
| isDescendentOfSingleProductTemplate | boolean | false |  |  |
| linkText | string |  |  |  |
| productId | number | 0 |  |  |
| showDescriptionIfEmpty | boolean | false |  |  |
| showLink | boolean | false |  |  |
| summaryLength | number | 0 |  |  |

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
```html
<!-- wp:woocommerce/product-summary {"productId":0,"isDescendentOfQueryLoop":false,"isDescendentOfSingleProductTemplate":false,"isDescendentOfSingleProductBlock":false,"isDescendantOfAllProducts":false,"showDescriptionIfEmpty":false,"showLink":false,"summaryLength":0,"linkText":""} /-->
```

---
## woocommerce/product-summary-field
**Title:** Product summary
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| allowedFormats | array | ["core/bold", "core/code", "core/italic", "core/link", "core/strikethrough", "core/underline", "core/text-color", "core/subscript", "core/superscript", "core/unknown"] |  |  |
| content | string |  |  |  |
| direction | string |  |  |  |
| helpText | string |  |  |  |
| label | string |  |  |  |
| property | string |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-summary-field
**Title:** Product summary
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| allowedFormats | array | ["core/bold", "core/code", "core/italic", "core/link", "core/strikethrough", "core/underline", "core/text-color", "core/subscript", "core/superscript", "core/unknown"] |  |  |
| content | string |  |  |  |
| direction | string |  |  |  |
| helpText | string |  |  |  |
| label | string |  |  |  |
| property | string |  |  |  |

### Supports
```json
{
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-tab
**Title:** Product tab
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| id | string |  |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-tab
**Title:** Product tab
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| id | string |  |  |  |
| title | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-tag
**Title:** Products by Tag
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alignButtons | boolean | false |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/product-tag {"columns":3,"rows":3,"alignButtons":false,"contentVisibility":{"image":true,"title":true,"price":true,"rating":true,"button":true},"tags":[],"tagOperator":"any","orderby":"date","isPreview":false} /-->
```

---
## woocommerce/product-tag-field
**Title:** Product Tag
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |
| name | string |  |  |  |
| placeholder | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-tag-field
**Title:** Product Tag
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| label | string |  |  |  |
| name | string |  |  |  |
| placeholder | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-taxonomy-field
**Title:** Taxonomy
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| createTitle | string |  |  |  |
| dialogNameHelpText | string |  |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| parentTaxonomyText | string |  |  |  |
| property | string |  |  |  |
| slug | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-taxonomy-field
**Title:** Taxonomy
**Category:** widgets
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| createTitle | string |  |  |  |
| dialogNameHelpText | string |  |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| parentTaxonomyText | string |  |  |  |
| property | string |  |  |  |
| slug | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-template
**Title:** Product Template
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/product-template /-->
```

---
## woocommerce/product-text-area-field
**Title:** Product textarea block
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| allowedFormats | array | ["core/bold", "core/code", "core/italic", "core/link", "core/strikethrough", "core/underline", "core/text-color", "core/subscript", "core/superscript", "core/unknown"] |  |  |
| direction | string |  |  |  |
| disabled | boolean |  |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| mode | string | rich-text |  |  |
| placeholder | string |  |  |  |
| property | string |  |  |  |
| required | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": true,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-text-area-field
**Title:** Product textarea block
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| allowedFormats | array | ["core/bold", "core/code", "core/italic", "core/link", "core/strikethrough", "core/underline", "core/text-color", "core/subscript", "core/superscript", "core/unknown"] |  |  |
| direction | string |  |  |  |
| disabled | boolean |  |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| mode | string | rich-text |  |  |
| placeholder | string |  |  |  |
| property | string |  |  |  |
| required | string |  |  |  |
| tooltip | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": true,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-text-field
**Title:** Product text field
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| help | string |  |  |  |
| label | string |  |  |  |
| max | object |  |  |  |
| maxLength | object |  |  |  |
| min | object |  |  |  |
| minLength | object |  |  |  |
| pattern | object |  |  |  |
| placeholder | string |  |  |  |
| property | string |  |  |  |
| required | object |  |  |  |
| suffix | object |  |  |  |
| tooltip | string |  |  |  |
| type | object |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-text-field
**Title:** Product text field
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| help | string |  |  |  |
| label | string |  |  |  |
| max | object |  |  |  |
| maxLength | object |  |  |  |
| min | object |  |  |  |
| minLength | object |  |  |  |
| pattern | object |  |  |  |
| placeholder | string |  |  |  |
| property | string |  |  |  |
| required | object |  |  |  |
| suffix | object |  |  |  |
| tooltip | string |  |  |  |
| type | object |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-title
**Title:** Product Title
**Category:** woocommerce-product-elements
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string |  |  |  |
| headingLevel | number | 2 |  |  |
| linkTarget | string |  |  |  |
| productId | number | 0 |  |  |
| showProductLink | boolean | true |  |  |

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
```html
<!-- wp:woocommerce/product-title {"headingLevel":2,"showProductLink":true,"productId":0} /-->
```

---
## woocommerce/product-toggle-field
**Title:** Product toggle control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkedHelp | string |  |  |  |
| checkedValue | object |  |  |  |
| disabled | boolean | false |  |  |
| disabledCopy | string |  |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| property | string |  |  |  |
| uncheckedHelp | string |  |  |  |
| uncheckedValue | object |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-toggle-field
**Title:** Product toggle control
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| checkedHelp | string |  |  |  |
| checkedValue | object |  |  |  |
| disabled | boolean | false |  |  |
| disabledCopy | string |  |  |  |
| help | string |  |  |  |
| label | string |  |  |  |
| property | string |  |  |  |
| uncheckedHelp | string |  |  |  |
| uncheckedValue | object |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": true
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-top-rated
**Title:** Top Rated Products
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alignButtons | boolean | false |  |  |
| catOperator | string | any |  |  |
| categories | array | [] |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| editMode | boolean | true |  |  |
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/product-top-rated {"columns":3,"rows":3,"alignButtons":false,"contentVisibility":{"image":true,"title":true,"price":true,"rating":true,"button":true},"categories":[],"catOperator":"any","isPreview":false,"editMode":true,"orderby":"rating"} /-->
```

---
## woocommerce/product-variation-items-field
**Title:** Product variations items
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| description | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-variation-items-field
**Title:** Product variations items
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| description | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-variations-options-field
**Title:** Product variations options
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| description | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/product-variations-options-field
**Title:** Product variations options
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| description | string |  |  |  |

### Supports
```json
{
  "__experimentalToolbar": false,
  "align": false,
  "html": false,
  "inserter": false,
  "lock": false,
  "multiple": true,
  "reusable": false
}
```

### Example Markup
_Not generated yet._

---
## woocommerce/products-by-attribute
**Title:** Products by Attribute
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| alignButtons | boolean | false |  |  |
| attrOperator | string | any |  |  |
| attributes | array | [] |  |  |
| columns | number | 3 |  |  |
| contentVisibility | object | {"button": true, "image": true, "price": true, "rating": true, "title": true} |  |  |
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/products-by-attribute {"attributes":[],"attrOperator":"any","columns":3,"contentVisibility":{"image":true,"title":true,"price":true,"rating":true,"button":true},"orderby":"date","rows":3,"alignButtons":false,"isPreview":false} /-->
```

---
## woocommerce/rating-filter
**Title:** Filter by Rating Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| displayStyle | string | list |  |  |
| isPreview | boolean | false |  |  |
| selectType | string | multiple |  |  |
| showCounts | boolean | false |  |  |
| showFilterButton | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/rating-filter {"className":"","showCounts":false,"displayStyle":"list","showFilterButton":false,"selectType":"multiple","isPreview":false} /-->
```

---
## woocommerce/related-products
**Title:** Related Products
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/related-products /-->
```

---
## woocommerce/reviews-by-category
**Title:** Reviews by Category
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/reviews-by-category /-->
```

---
## woocommerce/reviews-by-product
**Title:** Reviews by Product
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
_None_

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
```html
<!-- wp:woocommerce/reviews-by-product /-->
```

---
## woocommerce/single-product
**Title:** Product
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| isPreview | boolean | false |  |  |
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
```html
<!-- wp:woocommerce/single-product {"isPreview":true} /-->
```

---
## woocommerce/stock-filter
**Title:** Filter by Stock Controls
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| className | string |  |  |  |
| displayStyle | string | list |  |  |
| headingLevel | number | 3 |  |  |
| isPreview | boolean | false |  |  |
| selectType | string | multiple |  |  |
| showCounts | boolean | false |  |  |
| showFilterButton | boolean | false |  |  |

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
```html
<!-- wp:woocommerce/stock-filter {"className":"","headingLevel":3,"showCounts":false,"showFilterButton":false,"displayStyle":"list","selectType":"multiple","isPreview":false} /-->
```

---
## woocommerce/store-notices
**Title:** Store Notices
**Category:** woocommerce
**API Version:** 3
**Origin:** external
**Dynamic:** false

### Attributes
| Name | Type | Default | Source | Selector / Attr |
|---|---|---:|---|---|
| align | string | wide |  |  |

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
```html
<!-- wp:woocommerce/store-notices {"align":"wide"} /-->
```

---
