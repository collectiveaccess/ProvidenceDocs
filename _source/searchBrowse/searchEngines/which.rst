Which one do I use?
===================

For new installations use the default SqlSearch engine. It requires no special setup or configuration and can handle significant volumes of data. As your database grows you may elect to deploy ElasticSearch as it often provides significantly better performance than any other available engine. ElasticSearch does require a bit expertise to set up, however, and may be impractical to run on shared servers.

What about the others?
The MySQL FULLTEXT engine is still usable for 1.2 and earlier installations, if you don't want to change to SqlSearch, you don't have to. SqlSearch is basically an improved version of FULLTEXT; you should notice little if any disruption in the change.