---
name: Serene Editorial
colors:
  surface: '#faf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#faf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1a'
  on-surface-variant: '#444748'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f2f1ee'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#181919'
  on-primary: '#ffffff'
  primary-container: '#2d2d2d'
  on-primary-container: '#959494'
  inverse-primary: '#c8c6c6'
  secondary: '#625e55'
  on-secondary: '#ffffff'
  secondary-container: '#e8e2d6'
  on-secondary-container: '#68645b'
  tertiary: '#181816'
  on-tertiary: '#ffffff'
  tertiary-container: '#2d2d2a'
  on-tertiary-container: '#969490'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e4e2e1'
  primary-fixed-dim: '#c8c6c6'
  on-primary-fixed: '#1b1c1c'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#e8e2d6'
  secondary-fixed-dim: '#cbc6ba'
  on-secondary-fixed: '#1e1c14'
  on-secondary-fixed-variant: '#4a473e'
  tertiary-fixed: '#e5e2dd'
  tertiary-fixed-dim: '#c9c6c2'
  on-tertiary-fixed: '#1c1c19'
  on-tertiary-fixed-variant: '#474743'
  background: '#faf9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e3e2e0'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1120px
  gutter: 24px
  margin-mobile: 20px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

The design system is anchored in a sophisticated, editorial-inspired minimalism. It targets an audience that values slow consumption, clarity, and intellectual calm. The visual narrative rejects the frantic energy of typical social feeds in favor of a "digital sanctuary" aesthetic.

By blending **Minimalism** with **Tonal Layering**, this design system achieves a sense of physical presence—like high-quality stationery or a premium print magazine. The emotional response is one of reliability, warmth, and focused immersion. Whitespace is used aggressively as a functional element to reduce cognitive load and frame the content as the primary artifact.

## Colors

The palette is a curated spectrum of organic, warm tones designed to reduce eye strain and provide a premium tactile feel.

- **Primary (#2D2D2D):** A deep charcoal used for maximum legibility in text and iconography, providing a softer contrast than pure black.
- **Secondary (#E8E2D6):** A mid-tone warm beige for borders, dividers, and secondary button backgrounds.
- **Tertiary (#F5F2ED):** A soft cream used for container backgrounds and hover states to create subtle depth.
- **Neutral (#FAF9F6):** The base canvas color, mimicking high-grade off-white paper.
- **Accent (#C5B396):** A muted sand tone for focused highlights and subtle interactive cues.

## Typography

The typographic strategy utilizes a "Serif-on-Sans" pairing to balance traditional editorial authority with modern accessibility. 

**Newsreader** is reserved for headings to provide a literary, intellectual feel. Its variable weight allows for expressive, large-scale titles that feel elegant rather than aggressive. 

**Be Vietnam Pro** handles the functional and long-form reading aspects. Its friendly and contemporary structure ensures high legibility on mobile screens, even at smaller sizes. Labels use uppercase styling with increased letter-spacing to distinguish metadata from body narrative.

## Layout & Spacing

This design system employs a **Fixed Grid** on desktop and a **Fluid Margin** system on mobile. The primary content column is restricted to a narrow, readable width (max 720px for articles) within the larger container to ensure optimal line lengths for reading.

Vertical rhythm is strictly 8px-based. "Breathability" is the priority; use `stack-lg` between major sections to emphasize the minimal, airy nature of the brand. On mobile, margins should never shrink below 20px to prevent the content from feeling crowded against the device edges.

## Elevation & Depth

This design system avoids heavy shadows, instead using **Tonal Layers** and **Low-contrast outlines** to define hierarchy.

Depth is communicated by moving from the `Neutral` background to `Tertiary` surfaces. If a shadow is required for a floating element (like a mobile navigation menu), use a "Paper Shadow": a very soft, highly diffused #2D2D2D tint at 4% opacity with a large (24px+) blur. Dividers should be 1px solid lines using the `Secondary` color, creating a subtle, etched appearance.

## Shapes

The shape language is **Soft**, utilizing subtle 0.25rem (4px) corner radii. This creates a bridge between the sharp precision of modern digital interfaces and the organic softness of physical media. Large components like cards or hero images may use `rounded-lg` (8px), but never exceed this to ensure the design remains grounded and professional.

## Components

- **Buttons:** Primary buttons are solid `Primary` (Charcoal) with `Neutral` text. Secondary buttons are outlined in `Secondary` (Beige) with `Primary` text. All buttons use `label-md` typography.
- **Cards:** Cards use `Tertiary` backgrounds with no borders. Insets should be generous (24px-32px) to maintain the airy feel.
- **Input Fields:** Minimalist design with a 1px bottom border in `Secondary`. On focus, the border transitions to `Accent` (Sand). Use `body-md` for user input.
- **Chips/Tags:** Small, pill-shaped elements using `Secondary` backgrounds and `label-sm` text. They should have 0px elevation.
- **Lists:** Clean, unstyled list items separated by 1px `Secondary` dividers. Use custom bullet icons (small 4px squares in `Accent`).
- **Progressive Disclosure:** For blog-specific features, use "Reading Progress" bars in `Accent` at the top of the viewport, 2px in height, providing a subtle functional cue without distracting from the text.