## Amazon Dispute Manager

Amazon Dispute Manager is a Django-based application designed to assist Amazon sellers in efficiently managing and disputing return charges levied by Amazon. The application streamlines the process of filing and tracking disputes, empowering sellers to safeguard their interests, maintain account health, and ensure financial accuracy.


copy environment files and update the environment values, then run docker compose up

                        cp .env.dev.example .env.dev
                        docker build .
                        docker run -p 8000:8000
                        docker compose up -d


The application's APIs facilitate the creation of disputes and returns. To modify existing data, access the /admin console, where staff or admin users can make updates.


You can access the path /disputes to view disputes. This path utilizes HTMX for dynamic content loading.


### Model Tables -

            Order:

            Represents Amazon orders with fields such as order ID, item, and customer details.
            Return:

            Represents Amazon returns associated with specific orders, including return reason and tracking information.
            Dispute:

            Tracks dispute cases related to returns, including reasons for dispute and current status


