# Formatting Review: v1 -- tool-eval-bench on OpenShift

## Scores Table

| Dimension | Weight | Score (1-10) | Weighted Score |
|---|---|---|---|
| Heading hierarchy | 1x | 8 | 8 |
| Code formatting | 1x | 7 | 7 |
| CTA placement | 2x | 5 | 10 |
| SEO readiness | 1x | 5 | 5 |
| Link strategy | 1x | 4 | 4 |
| Editorial compliance | 2x | 6 | 12 |
| Brand standards | 1x | 6 | 6 |
| Word count | 1x | 9 | 9 |

**Weighted total: 61 / 100**

**Overall score: 6.1 / 10**

---

## Line-Level Feedback

### Heading hierarchy (8/10)

- Good: No H1 in body. All sections use H2, which cascades cleanly.
- Good: Most headings use sentence case correctly.
- Issue (line 59): "Deploying as batch evaluation Jobs" -- "Jobs" should be lowercase ("jobs") unless it's being used as a proper Kubernetes resource name. Since the heading is describing the general pattern, sentence case rules apply and it should be "Deploying as batch evaluation jobs."
- Issue (line 114): "Building automated model quality gates" -- correct sentence case, good.
- No skipped heading levels detected. No H3 subheadings are used, which is fine for this length.

### Code formatting (7/10)

- Good: Code blocks use proper fenced blocks with language tags (dockerfile, bash, yaml, python).
- Good: Code examples are real and runnable, not pseudocode.
- Issue: Backticks are used extensively in running text for inline code references: `pyproject.toml`, `README.md`, `src/`, `pip install .`, `--user`, `COPY`, `chown -R 1001:0`, `CrashLoopBackOff`, `--leaderboard`, `--diff RUN_ID`, `--short`, `--json`, `quay.io/aicatalyst/tool-eval-bench:latest`. The rubric explicitly states "no backticks" in final output. All inline code references must be reformatted (e.g., use monospace styling or italics depending on the publishing platform, but not markdown backticks).
- The mermaid diagram (lines 106-112) may not render on Red Hat Developer Blog. Confirm platform support or replace with a static image.

### CTA placement (5/10)

- Issue: There is no CTA near the top of the post. The abstract specifies a CTA ("Try deploying tool-eval-bench against your own model serving endpoint on OpenShift AI") but it only appears in the final section (line 141).
- Issue: No mid-article CTA. The "Why tool-calling quality matters" or "Test results" sections are natural insertion points for a mid-article CTA linking to Red Hat OpenShift AI product pages.
- The closing CTA (lines 141-155) exists but does not link to any redhat.com resource. It links only to the GitHub fork.
- Recommendation: Add a linked CTA to Red Hat OpenShift AI trial or product page near the top (after line 7 or line 13) and in the middle (after line 103). The closing CTA should include a link to redhat.com/openshift-ai or similar.

### SEO readiness (5/10)

- Issue: There is no title. The post starts with an H2 section heading ("What is tool-eval-bench?") rather than a proper blog title. A title like "Benchmarking LLM tool-calling quality on OpenShift AI with tool-eval-bench" (58 characters) would hit the 50-60 character sweet spot and contain target keywords.
- Good: The first paragraph (lines 3-4) mentions "open-weight LLMs," "tool calls," and the project name, providing keyword density.
- Issue: "Red Hat OpenShift AI" appears in the text but not in any heading or would-be title, reducing SEO impact for the target product.
- No meta description is provided.

### Link strategy (4/10)

- Issue: No links to redhat.com anywhere in the post. A blog on the Red Hat Developer Blog should link to relevant product pages (Red Hat OpenShift AI, Red Hat AI Inference Server).
- Link on line 5 goes to github.com (upstream project) -- acceptable.
- Link on line 156 goes to github.com/aicatalyst-team -- acceptable as the fork link.
- Issue: No internal links to related Red Hat developer content (e.g., other blog posts about model serving, OpenShift AI documentation, UBI image documentation).
- Recommendation: Add at least 2-3 redhat.com links: OpenShift AI product page, UBI image documentation, and Red Hat AI Inference Server page.

### Editorial compliance (6/10)

- Oxford commas: Mostly present. Line 5 uses "tool selection, parameter precision, multi-step chains, error recovery, safety boundaries, and more" -- correct. Line 17 uses "httpx, rich, and python-dotenv" -- correct.
- Issue (line 11): "A model that hallucinates function parameters, calls the wrong tool, or ignores safety constraints isn't just inaccurate: it's dangerous in production." -- Uses a colon where an em dash might be implied, but the colon is acceptable. Good use of contraction.
- Issue (line 5): "pass, partial, or fail" -- no Oxford comma issue, but consider whether these should be styled without backticks (currently no backticks, which is good).
- Product names:
  - "Red Hat OpenShift AI" (lines 7, 13, 143) -- correct full product name. Good.
  - "OpenShift" (lines 15, 49) -- acceptable shortened form after first full mention.
  - Issue: "Red Hat AI Inference Server" is referenced in the mermaid diagram (line 109) but never formally introduced in running text with its full official name. It should be introduced properly on first mention.
  - "UBI" (line 15) -- acronym is not expanded on first use. Should be "Universal Base Image (UBI)" on the first occurrence.
  - "CLI" (line 17) -- not expanded. Should be "command-line interface (CLI)" on first use.
  - "GSM8K, MMLU, IFEval" (line 5) -- these benchmark names are used without expansion. MMLU should be expanded: "Massive Multitask Language Understanding (MMLU)." GSM8K and IFEval should also be expanded or briefly described.
  - "PVC" (line 121) -- not expanded. Should be "persistent volume claim (PVC)."
  - "CI/CD" (line 126) -- not expanded. Should be "continuous integration/continuous delivery (CI/CD)" on first use.
  - "vLLM" (line 109 in mermaid, line 136 in code) -- appears only in code/diagram context, acceptable.
- Contractions: Good use throughout ("you've," "isn't," "don't," "can't," "it's").
- Em dashes: Line 17 uses a colon instead, which is fine. No em dashes detected -- good.
- Numerals: "69 deterministic scenarios" (line 5), "15 categories" (line 5), "3 Jobs" (line 63) -- correct use of numerals.
- Issue (line 63): "three Jobs" -- "three" should be "3" per the numerals rule. Also, "Jobs" is capitalized mid-sentence; lowercase unless referring specifically to the Kubernetes resource kind.

### Brand standards (6/10)

- Good: "Red Hat OpenShift AI" is correctly capitalized and named.
- Good: UBI9 image registry path is correct (`registry.access.redhat.com/ubi9/python-312`).
- Issue: The mermaid diagram references Red Hat brand colors (#EE0000, #A30000) which is a nice touch, but the diagram format may not render correctly on the target platform.
- Issue: No reference to Red Hat developer branding guidelines for the blog post header image or formatting.
- The Quay.io organization "aicatalyst" is used consistently.

### Word count (9/10)

- Estimated word count: ~1,050 words (excluding code blocks).
- This falls within the 800-1,300 word target range for a tutorial-style post.
- Good balance of prose and code examples.

---

## Editorial Compliance Checklist

| Rule | Status | Notes |
|---|---|---|
| Sentence case headings | PASS (minor issue) | "Jobs" capitalized in line 59 heading |
| Oxford commas | PASS | Consistently used |
| No backticks | FAIL | 15+ inline backtick usages throughout |
| Full product name on first mention | FAIL | "UBI," "CLI," "PVC," "CI/CD," "MMLU" not expanded |
| Lowercase component descriptors | PASS | No issues found |
| No H1 in body | PASS | All headings are H2 |
| Expand acronyms on first use | FAIL | Multiple unexpanded acronyms |
| Contractions | PASS | Good aggressive use |
| Numerals in running text | PASS (minor) | One instance of "three" vs "3" |
| Em dashes (max 1-2, no spaces) | PASS | No em dashes used |

---

## Summary

The draft is well-structured and technically solid, with a clean heading hierarchy and good use of contractions and Oxford commas. The word count is appropriate. However, it has 3 significant formatting issues that need attention before publication:

1. **Backticks must be removed.** Over 15 instances of inline backtick formatting violate the editorial standard. Replace with the appropriate styling for the publishing platform.

2. **CTA placement is insufficient.** The call to action only appears at the end. It needs to appear near the top and in the middle of the post, and it must link to redhat.com product pages, not just GitHub.

3. **Acronyms are not expanded on first use.** UBI, CLI, PVC, CI/CD, MMLU, GSM8K, and IFEval all need expansion on their first occurrence.

Secondary issues include missing redhat.com links, no blog title, and the "Red Hat AI Inference Server" product name not being formally introduced in running text.
