# Key-Value Store Flask App

The Key-Value Store Flask App is a simple web service that allows you to store and retrieve string values based on unique keys. It provides a lightweight and easy-to-use interface for managing key-value pairs in memory. The store is accessible through a RESTful API, making it convenient to integrate into your applications or interact with using command-line tools like `curl`.

The service also comes with a web-based dashboard that presents the current key-value store in a user-friendly table format. The dashboard automatically refreshes every 10 seconds, ensuring you always have the latest view of the stored data.

Please note that the Key-Value Store Flask App does not include any security measures and should be used only within a private network. Additionally, the stored data is volatile and not persisted across server restarts.

## Prerequisites

- Python 3.6 or higher

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/petermarks/key-value-store.git
    cd key-value-store
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv .venv
    ```

3. Activate the virtual environment:

    On macOS and Linux:

    ```bash
    source .venv/bin/activate
    ```

    On Windows:

    ```cmd
    .venv\Scripts\activate
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Start the Flask app:

```bash
flask run --reload
```

The `--reload` option enables automatic reloading of the app when code changes are detected.

Open your web browser and navigate to http://localhost:5000/dashboard to access the dashboard.

The dashboard displays the current key-value store in a table format. It automatically refreshes every 10 seconds to show the latest data.

## Interacting with the Service

You can interact with the key-value store service using curl or any other HTTP client. Below are some examples:

To store a value:

```bash
curl -X PUT -H "Content-Type: text/plain" -d "Hello, World!" http://localhost:5000/item/mykey
```

To retrieve a value:

```bash
curl http://localhost:5000/item/mykey
```

The response will contain the value associated with the key.

To retrieve the entire store as JSON:

```bash
curl http://localhost:5000/dump
```

The response will be a JSON object representing the current key-value store.

Please note that the `Content-Type` header is set to `text/plain` in the example above. Modify it accordingly if you store values in different formats.

## Running as a Service

To run the Key-Value Store Flask app as a service on Linux, follow these steps:

1. Create a file /etc/systemd/system/key-value-store.service with the following content:
    
    ```ini
    [Unit]
    Description=Key-Value Store Flask App
    After=network.target

    [Service]
    User=pi
    WorkingDirectory=/path-to-your-app
    ExecStart=/path-to-your-app/.venv/bin/python /path-to-your-app/key-value-store/app.py
    Restart=always

    [Install]
    WantedBy=multi-user.target
    ```
    
    Replace `path-to-your-app` in the ExecStart and WorkingDirectory fields to match the actual paths to your directory.

2. Reload systemd:

    ```bash
    sudo systemctl daemon-reload
    ```

3. Start the service and check it is running:

    ```bash
    sudo systemctl start key-value-store
    sudo systemctl status key-value-store
    ```

    The output should indicate whether the service is running properly.

4. Enable the service to start on boot:

    ```bash
    sudo systemctl enable key-value-store
    ```

    The will start automatically on boot and restart if it crashes or exits unexpectedly.

## License

This project is licensed under the [MIT License](LICENSE.txt).
