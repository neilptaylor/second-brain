---
name: client-folder-setup
description: >
  Set up the family-facing folder structure inside a client's Family Project
  Folder immediately after the new-client skill runs. Creates: 01 Plans,
  02 Guides (with children & parent reflection guides linked), 03 Trees,
  04 Photos, 05 Stories. Sets share permissions to Content manager so
  families can upload files. Pairs with client-onboarding-complete (which
  drafts the welcome email after the onboarding call).
---

# Client Folder Setup — Family-Facing Project Structure

Builds the client-side folder tree inside a family's project folder, ready
for them to start uploading guides, photos, and stories.

**Timing:** Run this immediately after `new-client` (which sets up the editing
folders). This creates the folders the family will see and use. Pair it with
`client-onboarding-complete` (which drafts and sends the welcome email once
dates are locked in).

## Before you start: gather these details

1. **Family surname** — exact spelling
2. **Tier** — Bronze, Silver, or Gold (this determines what guides exist)
3. **Children** — first names of all children, in order of their recording
   sessions (nil for Bronze)
4. **Parent(s)** — first name(s) and whether each is "Dad," "Mum," or a given
   name (check how Neil refers to them)
5. **Where the family folder already is** — Neil will have created this when
   he closed the sales call. Confirm the link or search Drive for
   `[Family Surname] - Families` under the Families root

Ask one clear question at a time if anything is ambiguous — getting the parent
names wrong means multiple folders get renamed later.

## Folder structure to create

Inside the family's project folder (e.g., `Pinkham - Families`), create exactly
5 folders in this order:

```
01 Plans
02 Guides
  ├── 01 Children
  │   └── [for each child: a subfolder with their name]
  └── 02 Parents
      └── [for each parent: a subfolder with their name]
03 Trees
04 Photos
05 Stories
```

**Bronze tier:** Same 5 folders. The 02 Guides folder still exists but will
only contain a "Parents" subfolder (no children).

## Inside each folder

- **01 Plans** — Empty. Family uses this for session prep notes.
- **02 Guides** — Has the two subfolders above (Children and Parents). Inside
  each child's folder, place a copy of the relevant reflection guide PDF.
  Inside each parent's folder, place: (a) their reflection guide PDF,
  (b) the audio version (if available), (c) the family life chart (if this
  family tier includes it). See "Linking guides" below.
- **03 Trees** — Empty. Family uploads family tree sketches/docs here.
- **04 Photos** — Empty. Family uploads old albums/photos here.
- **05 Stories** — Empty. Family dumps notes, memories, anything else here.

## Linking guides (the key step)

**DO NOT create new guides.** Neil's team produces these once the recording is
done. You're creating empty *slots* for them.

For each family, confirm which guides exist in the Families folder (search
for the family surname + "Reflection Guide" or "Life Chart"). Once you find
them:

1. **For each child:** Copy the child reflection guide PDF into their subfolder
   inside 02 Guides > 01 Children > [ChildName].
2. **For each parent:** Copy into their subfolder inside 02 Guides > 02 Parents
   > [ParentName]:
   - The parent reflection guide PDF
   - The audio version (usually .mp3, filename like "Parent Reflection Guide
     Audio.mp3")
   - The family life chart PDF (if this is a Silver or Gold project; Bronze
     may not have this)

If guides aren't yet in the Drive, leave those folders empty and flag it to
Neil — he'll drop them in later. Don't create placeholder docs.

## Share permissions (critical)

After creating all folders:

1. Open the top-level family folder (e.g., `Pinkham - Families`)
2. Click **Share** in the toolbar
3. Set **General access** to **"Anyone with the link"** → role **"Content
   manager"** (NOT Contributor, NOT Viewer — Content manager means they can
   upload and organize files)
4. Copy the shareable link

This link goes into the welcome email that `client-onboarding-complete` will
draft later.

## After building

Provide Neil with:

1. **The full folder tree** you created (list all 5 top folders + the subfolders
   inside 02 Guides, with parent/child names exactly as you named them)
2. **Guides status** — which guides you found and copied in, which are still
   missing
3. **The shareable link** to the family folder (the one you'll use in the
   welcome email later)
4. Screenshot or confirmation that share permissions are set to "Content
   manager"

Neil will eyeball this against the family's actual structure to catch name
mismatches before you draft the email.

---

## Next step: client-onboarding-complete

Once Neil confirms the session times (after the onboarding call with the
family), run `client-onboarding-complete` to draft the welcome email. That
skill will:

- Address the family by name
- Link to this folder you just created
- List all upcoming session times (pulled from Neil's calendar)
- Link to the specific children guides, parent guides, trees, and photos
  folders
- Convert times to their timezone

Don't draft the email in this skill — just get the folders right. The email
skill will handle all the customer-facing copy.
