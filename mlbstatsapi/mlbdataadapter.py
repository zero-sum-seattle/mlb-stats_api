import requests
from typing import List, Dict
from .exceptions import TheMlbStatsApiException
import logging



class MlbDataAdapter:
    """Adapter for calling the mlb statsapi endpoint"""

    def __init__(self, hostname: str = 'statsapi.mlb.com', ver: str = 'v1', logger: logging.Logger = None):
        self.url = f"https://{hostname}/api/{ver}/" # we'll figure out the v1.1 endpoint later
        self._logger = logger or logging.getLogger(__name__)


    def get(self, endpoint: str, data: Dict = None) -> List[Dict]:
        full_url = self.url + endpoint # pass endpoint from inhertited classes
        logline_pre = f"url={full_url}"
        logline_post = f" ,".join((logline_pre, "success={}, status_code={}, message={}"))
        try: 
            self._logger.debug(logline_post)
            response = requests.get(url=full_url) # mlbstats API only uses get calls

        except requests.exceptions.RequestException as e: # catch a response error
            self._logger.error(msg=(str(e))) # log error 
            raise TheMlbStatsApiException("Request failed") from e

        try:
            data = response.json()
        except (ValueError, requests.JSONDecodeError) as e: # catch a JSON error
            self._logger.error(msg=(str(e))) # log error JSON 
            raise TheMlbStatsApiException("Bad JSON in response") from e
        if response.status_code <= 200 and response.status_code <= 299: # catch HTTP errors
            self._logger.debug(msg=logline_post.format("success", response.status_code, response.reason)) # log success 
            return MlbResult(response.status_code, message=response.reason, data=data) # return result

        raise TheMlbStatsApiException(f"{response.status_code}: {response.reason}") # raise exception 





class MlbResult:
    def __init__(self, status_code: int, message: str, data: List[Dict]):
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []