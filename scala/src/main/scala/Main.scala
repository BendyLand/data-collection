import scala.io.*

enum LogType:
    case Request, LogMessage

@main def run() =
    val file = readFile()
    val lines = file.split('\n')
    val logTypes = lines.map(line => classifyLogType(line))
    val pairs = lines.zip(logTypes)
    val times = pairs.map(pair => parseTime(pair))
    times.foreach(println)

def parseTime(pair: (String, LogType)): (String, String) =
    var date = ""
    var time = ""
    pair._2 match
        case LogType.Request =>
            var tempStr = pair._1.dropWhile(_ != '[')
            val end = tempStr.indexOf('+')
            tempStr = tempStr.substring(1, end-1)
            val items = tempStr.split(":", 2)
            date = items(0)
            time = items(1)
        case LogType.LogMessage => 
            val tempStr = pair._1.split(" ")(0)
            val items = tempStr.split("T")
            date = items(0)
            time = items(1)
    (date, time)

def classifyLogType(log: String): LogType =
    if log.contains("HTTP/1.1") then
        LogType.Request
    else
        LogType.LogMessage


def readFile(): String =
    val file = Source.fromFile("sample_logs.txt")
    try file.mkString finally file.close()
