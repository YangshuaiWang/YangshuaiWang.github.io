---
title: Talks & Conferences
summary: Invited talks and minisymposium organization by Yangshuai Wang.
type: landing
cms_exclude: true
sections:
  - block: side-section
    id: talks-heading
    content:
      heading_level: 1
      title: Talks & Conferences
      text: Invited talks and minisymposium organization.
  - block: side-collection
    id: invited-talks
    content:
      title: Invited talks
      count: 0
      filters:
        folders: [conferences]
        exclude_tag: organizer
    design:
      view: citation-talk
  - block: side-collection
    id: organization
    content:
      title: Organization
      count: 0
      filters:
        folders: [conferences]
        tag: organizer
    design:
      view: citation-talk
---
