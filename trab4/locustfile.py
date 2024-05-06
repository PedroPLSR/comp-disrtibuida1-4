from locust import HttpUser, between, task

class WikipediaUser(HttpUser):
    host = "http://localhost"
    wait_time = between(5, 10)
    
    urls_for_testing = [
        "https://github.com/features/actions",
        "https://github.com/Blealtan/efficient-kan",
        "https://github.com/karpathy/llm.c",
        "https://github.com/marketplace/naming-conventions-bot",
        "https://github.com/AthenZ/athenz",
        "https://github.com/huggingface/candle",
        "https://github.com/fastfetch-cli/fastfetch",
        "https://github.com/adrianhajdin/banking",
        "https://github.com/tokio-rs/axum",
        "https://github.com/codecrafters-io/build-your-own-x"
    ]

    @task
    def load_test(self):
        for url in self.urls_for_testing:
            self.client.get(f"/?url={url}")
