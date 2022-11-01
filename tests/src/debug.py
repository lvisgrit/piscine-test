import debugpy
import main

if __name__ == "__main__":
    debugpy.listen(5678)
    debugpy.wait_for_client()
    main.entrypoint()
