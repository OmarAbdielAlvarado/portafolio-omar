# compliance-rewriter (vod-pipeline)
Production component of an automated VOD pipeline (2026): rewrites video SEO
metadata (titles/descriptions/tags, Spanish + English) to enforce Visa &
Mastercard content policies (prohibited-terms lists) before publishing.
Rules are data, not code -> new networks/locales without touching logic.
Dockerized Flask blueprint. Ran in production, single-server.
Run: docker build -t cr . && docker run -p 8000:8000 -v $PWD/data:/data cr
Test: curl localhost:8000/api/compliance-seo/scene_001
