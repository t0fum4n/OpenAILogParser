# syslogparser.py

# ailogparser
This is a private repo for my ai log parser code

This is a POC of parseing different log types into different formats. One of the pain points in the cyber security industry is making sense of all the different log source types from all your diffent sources. This tool aims to start the conversation of using AI to parse our logs. 

Examples. 
  Create regex string for a syslog message
  Create a json format blob from a syslog message
  create a syslog message from a json blob
  
Other uses.
  create LLM specifically for log set from siem or other database of logs and use that LLM to parse new incoming logs
  tokenize log databases and compare incoming logs to those tokens. ( Malware = virus / trojan / mware). Having a LLM specifically for your log data set will give it the   ability to learn patterns for the logs. (anomolous logins, malware patterns, geo ip patterns for users, etc)

The application of AI to the cyber security world seems inevitable. I started thinking about this topic when the matter of trying to ingest a new log source type into a SIEM. 

Creating the regex pattern needed for the SIEM to parse the logs into their respective fields was a difficult task. One that the company I work for was willing to pay for professional support services to get a new log source onboarded. 

The SIEM has many different ways it can ingest logs but most of them end in parsing a syslog message with regex and then putting that into a DB. 

This tool can help in the creation of the regex pattern that is needed to parse the log into it's respective fields into the SIEM DB. It's not perfect. But toying around with the prompt to OpenAI can produce a result that is darn close if not exactly what you need. 

I also envision this tool as a way to generate syslog from Json. One could make an API call to an endpoint and take the response and use OpenAI to convert it to syslog and forward that to the ingestion mechanism for the SIEM. Obviously this would get resource intensive so you likely won't do EVERY log... But it would help in building the structure that one would need to take a new Json prompt that has never been parsed before and convert it to syslog. Or vice versa. 

Ultimately having ones own LLM who's dataset is the log / event database is what I envision. Tokenizing each field after it is parsed within a log DB and using an interface to make calls to that AI to then use the data that is contained in the SIEM logs to produce a result. 

One of the issues I've had working with logs is that sometimes things get parsed into the wrong field. An ip address will be in a hostname field for example. Well. Training ones own LLM and using it to make decisions on logs to decide what is an IP address. What is a Mac address. What is a port. Etc. 

I am no expert at literally anything. I work in the cyber security field and I saw a glimpse of what could be months and months ago. The idea has been bouncing around in my head since then. 

I saw ChatGPT in the news and started playing with it. At first I thought, oh cool. I can help with my kids homework... 

Then I realized it could write tweets for me based on information I gave it. 

Then I had it writing emails for me. I fed it the contents of the original email and it spat back what the response should be. 

Then I asked it some things that I didn't think it would be able to handle. 

What is God? Is God real?

Obviously those produced expected results. 

But then I asked it to parse out a syslog message for me. 

And it... Kinda did it. 

And that's when the light kicked on. 

I can use LLM to parse my logs for me. I don't have to write the regex. I can ask ChatGPT to do it for me. And it....did it. 

So I decided I wanted to package this and make it something cool. I started on two projects. One for log messages. One for using AI to create tweets for me. 

Both make use of the openai API. 

I believe I am the first person to use OpenAI this way and I think it could really revolutionize cyber security for organizations. 

Each org having their own LLM specific to their log databases. 

What I would like to build is a docker container that has this code on it that will run some software that latches on to a siems dB's and begins the process of it and doing its learning. This will grow and expand overtime. I am posting this as some sort of timestamp of my progress. To prove it. To myself I guess. 



Example Syslog parsed via regex

Parse the following log file with regex and give me the pattern that matches it

| Source IP | Destination IP | Source Port | Destination Port | Source MAC |

Tue Mar 04 15:57:06 2020: <14>Mar  4 15:53:03 BAR-NG-VF500 BAR-NG-VF500/box_Firewall_Activity:  Info     BAR-NG-VF500 Remove: type=FWD|proto=UDP|srcIF=eth1|srcIP=192.168.70.7|srcPort=35119|srcMAC=08:00:27:da:d7:9c|dstIP=8.8.8.8|dstPort=53|dstService=domain|dstIF=eth0|rule=InternetAccess/<App>:RestrictTim|info=Balanced Session Idle Timeout|srcNAT=192.168.70.7|dstNAT=8.8.8.8|duration=21132|count=1|receivedBytes=130|sentBytes=62|receivedPackets=1|sentPackets=1|user=|protocol=|application=|target=|content=|urlcat
=|

Pattern: \|srcIP=([\d.]+)\|srcPort=(\d+)\|srcMAC=([\w:]+)\|dstIP=([\d.]+)\|dstPort=(\d+)\|
  
  ![image](https://user-images.githubusercontent.com/12946325/210158248-5d71df02-8e6a-4adc-8f86-de4ec40e482d.png)

  
 As you can see it is NOT perfect. BUt it did parse out the information i was looking for from the syslog file with a regex pattern that matches that log string.
 
 
 Another example of me asking it to take a syslog file and parse it for me into a table
 
 Take the following syslog file and parse out the important parts such as - | Source IP | Destination IP | Source Port | Destination Port | Source MAC | - and put the data in a table

Tue Mar 04 15:57:06 2020: <14>Mar  4 15:53:03 BAR-NG-VF500 BAR-NG-VF500/box_Firewall_Activity:  Info     BAR-NG-VF500 Remove: type=FWD|proto=UDP|srcIF=eth1|srcIP=192.168.70.7|srcPort=35119|srcMAC=08:00:27:da:d7:9c|dstIP=8.8.8.8|dstPort=53|dstService=domain|dstIF=eth0|rule=InternetAccess/<App>:RestrictTim|info=Balanced Session Idle Timeout|srcNAT=192.168.70.7|dstNAT=8.8.8.8|duration=21132|count=1|receivedBytes=130|sentBytes=62|receivedPackets=1|sentPackets=1|user=|protocol=|application=|target=|content=|urlcat
=|

| Source IP | Destination IP | Source Port | Destination Port | Source MAC |
|:----------|:---------------|:------------|:-----------------|:-----------|
| 192.168.70.7 | 8.8.8.8 | 35119 | 53 | 08:00:27:da:d7:9c |

  
Example of using davinci-003 to parse xml logs into a table with criteria tht are "like" the fields in the xml example
  
  Parse these fields from the following xml log file.

| Name | Employee ID | Start Date |

<xml>
   <name firstName="John" lastName="Doe" />
   <employeeId>12345</employeeId>
   <other>ignore</other>
   <dateJoined>2014-05-16 10:50:14,125</dateJoined>
</xml>


Name: John Doe
Employee ID: 12345
Start Date: 2014-05-16 10:50:14,125

Process finished with exit code 0

  ![image](https://user-images.githubusercontent.com/12946325/210185887-f28cc4d3-31dc-4ca9-a3ee-1fe147ad581f.png)
  
  
Thinking about this. The hardest part of ingesting log sources here is classifying things via regex into dedicated fields. One could store a log message as a simple string of text and then tokenize the items in that string. Another model could then make decisions based on those tokens. For example. 

the string "Malware has the token value of [15029, 1574] according to https://beta.openai.com/tokenizer
the tring "malware" has the token value of [7617, 1574] according to the same source. 

Now it doesnt take a data scientist to be able to tell that two of those tokens are alike.... 1574. The other two tokens are completely different however any person can tell that [15029, 1574] and [7617, 1574] are similar... even if Malware does not = malware

This is obviously a simple example as this as far as my human brain can comrehend. This is why we have LMM's. 
