/{repository}/{environment}/{doc_id}
====================================

get
---

Description:

    Request for a document in repository to be indexed.

Parameters:

      repository (path parameter)

      environment (path parameter)

      doc_id (path parameter)

      type (query parameter)

Responses:

    200: Returns {'status': 'queued'}

    500: Returns {'status': 'error'}

