---
title: Selected Preprints
summary: Selected preprints, submitted manuscripts, and other writing by Yangshuai Wang.
type: landing
cms_exclude: true

design:
  spacing: '5rem'

sections:
  - block: side-section
    id: preprints-heading
    content:
      heading_level: 1
      title: Selected Preprints
      text: |-
        Selected preprints and submitted manuscripts. Public versions are linked where available.

        [Published and accepted papers →](/publications/)
  - block: side-collection
    id: preprint-list
    content:
      title: Preprints & submissions
      count: 0
      sort_by: source_order
      numbered: true
      filters:
        folders:
          - publications
        tag: preprint
        exclude_featured: false
    design:
      view: citation
  - block: side-collection
    id: book
    content:
      title: Book
      count: 0
      filters:
        folders: [publications]
        tag: book
    design:
      view: citation
  - block: side-collection
    id: thesis
    content:
      title: Doctoral thesis
      count: 0
      filters:
        folders: [publications]
        tag: thesis
    design:
      view: citation
---
