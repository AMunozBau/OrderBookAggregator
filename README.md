# OrderBookAggregator

## How to Run

To run this application from the console, follow these steps:

1. Make sure you have Python installed on your system.
   
3. Create or activate a virtual enviroment and instal all requirements

    ```bash
   pip install -r requirements. txt
    ```

4. Open a terminal or command prompt.

5. Navigate to the directory where your main script is located. Use the `cd` command to change directories:

    ```bash
    cd path/to/your/script
    ```

6. Run the script using the following command:

    ```bash
    python main.py
    ```

## Optional Arguments

You can pass optional arguments when running the script:

- To specify a target amount (Default value is 10):

    ```bash
    python main.py 15
    ```

    Replace `15` with the desired target amount.

- To use the Kraken exchange(Default value is False):

    ```bash
    python main.py 15 true
    ```

    Replace `15` with the target amount, and `true` to indicate the use of the Kraken exchange.
