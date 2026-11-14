# DP-800 SQL and AI portfolio projects

Three planned case studies for the Secure Multi-Cloud Business Platform. They share a fictional retailer, synthetic products and orders, and an authorized read path for reports and document search.

## 1. Secure sales reporting

- **Build:** Extend the private Azure SQL lab with a small passwordless report reader. Use regional row-level security, scoped object permissions, an encryption test, and database auditing. Package the schema as an SDK-style SQL database project and validate changes in GitHub Actions.
- **Prove:** East and West readers see their own rows. A write by the reporting identity is denied. A deliberately unsafe schema change fails CI. Keep the audit record and use a date-range query to verify partition elimination if monthly partitioning is added.
- **Evidence:** Role and test matrix, sanitized query results, audit record, and pipeline output. The earlier Azure SQL lab already recorded SELECT success and INSERT error 229. The integrated report reader and new controls are planned.

## 2. Product catalog and order API

- **Build:** Use typed columns for SKU, price, and category, with JSON for category-specific attributes. Add constraints and a transactional order procedure with error handling. Expose a read endpoint with Data API Builder. Use a shared invoice sequence only if gaps meet the numbering requirement.
- **Prove:** A valid order commits, an invalid order rolls back, and an indexed catalog filter returns identical rows with fewer logical reads. Compare a typed computed-column index with a native JSON index if the database supports it.
- **Evidence:** Schema, seed data, transaction tests, sample API request, and before-and-after execution plans.

## 3. Catalog and policy search assistant

- **Build:** Chunk and embed synthetic manuals, descriptions, and policies. Compare full-text, exact vector, and hybrid retrieval on 20 labeled questions. Use approximate vector search only after checking support on the selected SQL target. Apply caller permissions before passing retrieved chunks to the model.
- **Prove:** Measure top-five retrieval accuracy and latency. Demonstrate a sourced answer, a question declined for insufficient evidence, and a restricted document excluded before the model call.
- **Evidence:** Labeled questions, retrieval measurements, and sanitized authorization and answer tests.

Build after the remaining SC-500 labs in the order above. Publish each case study with reproducible setup steps and actual test results as work is completed.

- [Portfolio roadmap](https://aesthetic-pudding-79f963.netlify.app/architecture#dp800-projects)
- [Microsoft DP-800 skills outline](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-800)
