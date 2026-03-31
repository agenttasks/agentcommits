---
name: research-account-setup
description: |
  Guides research and account setup for social media platform APIs. Covers
  developer account creation, API registration, and initial configuration
  for TikTok, Instagram, YouTube, and Higgsfield AI content publishing.
allowed-tools: Read, Write, Bash
---

# Research & Account Setup

Guide the user through setting up developer accounts and API access for social
media content publishing platforms.

## Supported Platforms

- **TikTok** -- Creator/Business account with Content Posting API access
- **Instagram** -- Business account via Meta Business Suite and Instagram Graph API
- **YouTube** -- Channel with YouTube Data API v3 via Google Cloud
- **Higgsfield AI** -- API key for AI video generation

For detailed per-platform setup steps, see [references/platform-setup.md](references/platform-setup.md).

## Setup Workflow

1. Identify which platforms the user needs configured.
2. Walk through account creation and developer portal registration for each.
3. Register the app and request required API scopes/permissions.
4. Collect and store credentials as environment variables (never in version control).
5. Verify credentials are set by checking required environment variables.

## Credential Verification

Check that all required environment variables are present for each configured
platform:

- **TikTok**: `TIKTOK_CLIENT_KEY`, `TIKTOK_CLIENT_SECRET`, `TIKTOK_ACCESS_TOKEN`
- **Instagram**: `META_APP_ID`, `META_APP_SECRET`, `INSTAGRAM_ACCESS_TOKEN`, `INSTAGRAM_BUSINESS_ACCOUNT_ID`
- **YouTube**: `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `YOUTUBE_REFRESH_TOKEN`, `YOUTUBE_CHANNEL_ID`
- **Higgsfield**: `HIGGSFIELD_API_KEY`

## Research Checklist

When setting up a new platform, research and document:

1. Current API rate limits and quotas
2. Content policy and community guidelines
3. Optimal content specifications (resolution, codec, bitrate)
4. Analytics API availability for measurement
5. Webhook availability for real-time notifications

## Handoff

After setup is complete, generate a requirements document for platform-engineering
containing:

- Confirmed API access per platform
- Rate limits and quotas discovered
- Content specifications validated
- Credential storage confirmation (environment variables only)
