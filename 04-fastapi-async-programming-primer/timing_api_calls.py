import uvicorn
from main import app
from contextlib import contextmanager
from multiprocessing import Process
import asyncio
from httpx import AsyncClient
import time 

def run_server():
    """
    Run the FastAPI server with Uvicorn.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)


@contextmanager
def run_fastapi_server():
    """
    Context manager to run the FastAPI server in a separate process.
    """
    process = Process(target=run_server)
    process.start()

    # Wait for the server to start
    import time
    time.sleep(5)
    print("FastAPI server is running in a separate process...")
    try:
        yield
    finally:
        process.terminate()
        
## Now we can define a function that makes n API calls to the server
async def make_api_calls(n: int, path: str):
    """
    Make n API calls to the specified path.
    """
    async with AsyncClient() as client:
        tasks = [client.get(f"http://localhost:8000{path}", timeout=float("inf")) for _ in range(n)]
        responses = await asyncio.gather(*tasks)
        
        #return [response.json() for response in responses]
        
async def main(n: int = 10):
    """
    Main function to run the FastAPI server and make API calls.
    """
    with run_fastapi_server():
        print("Making API calls...")
        # Make synchronous and asynchronous API calls
        start_time = time.time()
        # Make synchronous API calls
        await make_api_calls(n, "/sync")
        end_time = time.time()
        sync_time_diff = end_time - start_time
        print(f"Synchronous API calls took {sync_time_diff:.2f} seconds.")
        # Make asynchronous API calls
        start_time = time.time()
        await make_api_calls(n, "/async")
        end_time = time.time()
        async_time_diff = end_time - start_time
        print(f"Asynchronous API calls took {async_time_diff:.2f} seconds.")

        
        print(f"Made {n} synchronous API calls: {sync_time_diff:.2f} seconds")
        print(f"Made {n} asynchronous API calls: {async_time_diff:.2f} seconds")

        return {'n': n, "sync_time": sync_time_diff, "async_time": async_time_diff}

if __name__ == "__main__":
    result = []
    n = 10  # Number of API calls to make
    result.append(asyncio.run(main(n)))
    print(f"\nAll {n} API calls completed for both synchronous and asynchronous methods.\n\n")

    n = 100  # Number of API calls to make
    result.append(asyncio.run(main(n)))
    print(f"\nAll {n} API calls completed for both synchronous and asynchronous methods.\n\n")

    print(result)

# This code runs a FastAPI server in a separate process and makes multiple synchronous and asynchronous API calls to it.