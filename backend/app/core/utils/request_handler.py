import requests
from requests.exceptions import HTTPError, RequestException
import logging
from typing import Optional, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def make_request(
    method: str,
    url: str,
    headers: Optional[Dict[Any, Any]] = None,
    params: Optional[Dict[Any, Any]] = None,
    json: Optional[Dict[Any, Any]] = None,
) -> Any:
    """
    Makes an HTTP request and returns the JSON response.

    Args:
        method (str): HTTP method (GET, POST, PUT, DELETE).
        url (str): Full URL of the request.
        headers (dict): Request headers.
        params (dict): Query parameters.
        json (dict): JSON payload for POST/PUT requests.

    Returns:
        dict: JSON response.

    Raises:
        HTTPError: If the HTTP request fails.
    """
    try:
        logger.info(
            f"Making {method} request to {url} with headers: {headers} and params: {params}"
        )

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            timeout=10,  # Timeout in seconds
        )

        # Raise exception for HTTP errors
        response.raise_for_status()

        # Log and return the response JSON
        if response.status_code != 204:  # No content
            print(f"Response JSON: {response.json()}")
            response_json = response.json()
            logger.info(f"Response JSON: {response_json}")
            return response_json

        # Return an empty dict for successful responses with no content
        return {}

    except HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        raise http_err
    except RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")
        raise req_err
    except Exception as err:
        logger.error(f"Unexpected error occurred: {err}")
        raise err
