curl --request POST   --url https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json   --header 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAAC8jkgEAAAAAD2OkgxssdZuu%2BmVB34ZjFnvjW6M%3DWUEdNZE8UjyWmyroGfZAAWvLPCMEKcA2MlqOCKbX4bnOmgWSe4'  --header 'content-type: application/json'   --data '{
                "query":"SMN_OCBA lang:es",
                "maxResults": "100",
                "fromDate":"201701010101",
                "toDate":"201801010101"
                }'    > archivo