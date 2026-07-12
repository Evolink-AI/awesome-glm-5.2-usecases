# Media Inventory, R2 Upload, and Origin Audit

- Audit date: 2026-07-12
- Public media directory: `images/`
- Media files inventoried: 2
- Policy: shared R2 brand banner and stable Star History snapshot across all 11 README files
- Expected bucket: `image`
- Expected public base URL: `https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev`
- Expected key prefix: `github-repo-media`

## Inventory

| Local source | Type | Dimensions | Size | Public usage |
|---|---|---:|---:|---|
| `images/en.jpg` | JPEG image | 1774×887 | 142,123 bytes | Shared banner in 11 README files |
| `images/star-history.svg` | SVG image | 900×420 | generated deterministically | Shared Star History snapshot in 11 README files |

## Runtime And Identity Preflight

- Python runtime imported `boto3`: PASS
- Bucket identity: `image` — PASS
- Public base identity: `https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev` — PASS
- Key-prefix identity: `github-repo-media` — PASS
- Note: the inherited default was `model-repo-media`; this run explicitly locked `R2_KEY_PREFIX=github-repo-media` before upload.

## Upload Result

- Markdown files scanned: 11
- Media files uploaded: 2
- Markdown files rewritten: 11
- Uploaded object: `github-repo-media/awesome-glm-5.2-usecases/images/en.jpg`
- Public URL: `https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/en.jpg`
- Uploaded object: `github-repo-media/awesome-glm-5.2-usecases/images/star-history.svg`
- Public URL: `https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/awesome-glm-5.2-usecases/images/star-history.svg`

## Origin Verification

- HTTP status: `200`
- Content-Type: `image/jpeg`
- Final URL matches the locked R2 public URL: PASS
- README width: `760`
- Alt text: present and localized in all 11 README files

## Star History Fallback

- GitHub metadata at snapshot: repository created `2026-07-04`; `0` stars on `2026-07-12`.
- The live `api.star-history.com` SVG endpoint returned repeated HTTP 500/504 timeouts for this new zero-star repository.
- `scripts/build_star_history.py` generates a deterministic SVG that states the current count and explicitly does not infer a historical trend.
- The chart remains linked to the canonical Star History page; only the unstable embedded image is replaced by the R2-hosted snapshot.

## Rendered GitHub Verification

Post-push GitHub/camo verification is required before the modification can be reported as `published`. It is intentionally not marked passed from R2 origin evidence alone.
