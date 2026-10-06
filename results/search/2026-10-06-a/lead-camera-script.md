# Disposable-camera skill, script unread

Finding `camera-script`. Draft.

Grade: lead, thin. Will: hidden behavior, only if the unread script does something the markdown does not say.

Severity: unknown until the script is read. Uptake: the listing reports 12 installs and 658 downloads. That is a registry counter, not a shown use of a hidden behavior. Attribution: publisher `blammectrappora`.

## Opened

`GET https://clawhub.ai/api/v1/skills/disposable-camera-photo-generator` on 2026-10-06 returned the skill record. Slug `disposable-camera-photo-generator`. Summary and the markdown in `description` say it generates photos through the Neta image API and that the caller passes that API's own token on the command line. `isSuspicious` is false. Version id `k97efvc89q8enwe9sbxrw935yd85v0cp`. `sourceUrl` is null.

The markdown does not mention a credential file, a webhook, or hiding the call. The token it asks for is the token of the image service it names.

## Not opened

`GET .../versions/k97efvc89q8enwe9sbxrw935yd85v0cp` returned "Version not found". `GET .../blammectrappora/disposable-camera-photo-generator/files` returned "Not found". `blammectrappora/disposable-camera-photo-generator` on GitHub was 404. The script named in the markdown, `disposablecameraphotogenerator.js`, was not read.

## What would kill it

The script only calls the Neta host the markdown names, and only sends that service the token the caller passed for it.

## Next

One public file URL for that script, read as text. If none exists, keep the lead and stop retrying until a new pointer appears.
