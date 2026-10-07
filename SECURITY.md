# Security Policy

## Supported version

Security fixes are applied to the latest commit on `main`.

## Reporting a vulnerability

Please do not open a public issue for a suspected vulnerability or exposed credential. Contact the repository owner through the GitHub profile instead. Include the affected component, reproduction steps, and possible impact. Do not attach real resumes, personal information, access tokens, or passwords.

## Public demo boundary

- The repository contains synthetic resumes, job records, and a local demo account only.
- `.env.example` contains placeholders. Real secrets must be stored outside Git and rotated if exposed.
- Default database passwords and demo credentials are for local development only.
- Resume files are sensitive personal information. Production deployments require encryption, retention rules, deletion support, malware scanning, access auditing, and strict authorization.
- Recommendations are decision support only and must not be used to automatically reject candidates.
