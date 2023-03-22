# mtg-price-tool
 A tool for pricing mtg cards. Uses scraped data from MTGGoldfish


## Usage
 1.) Set `./set_details/list.txt` to include the sets that you want to scrape. (You must have the related json in `set_details`... not all of these exist yet.)  
 2.) Run `./python3 price_checker.py`  
 3.) Data will populate in `./daily_output`
## Future Plans
 - Add more sets
 - Clean up sets to only check for certain things
 - Load tracked prices into memory, build a UI to better organize and use this data
