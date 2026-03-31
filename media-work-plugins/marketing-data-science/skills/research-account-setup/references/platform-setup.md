# Platform Setup Guides

## TikTok

1. Upgrade to a TikTok Creator or Business account.
2. Register at developers.tiktok.com.
3. Create an app for the Content Posting API.
   - Required scopes: `video.publish`, `video.upload`
   - App review and approval takes 5-10 business days.
4. Store credentials:
   - `TIKTOK_CLIENT_KEY` -- app key
   - `TIKTOK_CLIENT_SECRET` -- app secret
   - `TIKTOK_ACCESS_TOKEN` -- OAuth token

## Instagram (via Meta Business Suite)

1. Convert to an Instagram Business or Creator account.
2. Link the Instagram account to a Facebook Page.
3. Register at developers.facebook.com.
4. Create an app with the Instagram Graph API.
   - Required permissions: `instagram_content_publish`, `pages_read_engagement`
   - App review required for publishing permissions.
5. Store credentials:
   - `META_APP_ID` -- app ID
   - `META_APP_SECRET` -- app secret
   - `INSTAGRAM_ACCESS_TOKEN` -- long-lived token
   - `INSTAGRAM_BUSINESS_ACCOUNT_ID` -- account ID

## YouTube (via Google Cloud)

1. Create or use an existing YouTube channel.
2. Create a project at console.cloud.google.com.
3. Enable the YouTube Data API v3.
4. Create OAuth 2.0 credentials for a desktop app.
   - Required scopes: `youtube.upload`, `youtube.readonly`
5. Store credentials:
   - `GOOGLE_CLIENT_ID` -- client ID
   - `GOOGLE_CLIENT_SECRET` -- client secret
   - `YOUTUBE_REFRESH_TOKEN` -- refresh token
   - `YOUTUBE_CHANNEL_ID` -- channel ID

## Higgsfield AI

1. Sign up at higgsfield.ai.
2. Request an API key from settings or the contact page.
3. Verify sufficient credits for video generation.
4. Store credentials:
   - `HIGGSFIELD_API_KEY` -- API key
