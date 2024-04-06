import scala.io.*

enum LogType:
    case Request, LogMessage
@main def run() =
    val file = readFile()
    val lines = file.split('\n')
    val logTypes = lines.map(line => classifyLogType(line))
    val pairs = lines.zip(logTypes)
    pairs.foreach(println)


def classifyLogType(log: String): LogType = 
    if log.contains("HTTP/1.1") then
        LogType.Request
    else
        LogType.LogMessage


def readFile(): String = 
    val file = Source.fromFile("sample_logs.txt")
    try file.mkString finally file.close()
