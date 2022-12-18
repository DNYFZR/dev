// @main def hello: Unit = 
//   println("Hello world!")
//   println(msg)

// def msg = "I was compiled by Scala 3. :)"


@main
val spark:SparkSession = SparkSession.builder()
   .master("local[1]").appName("SparkByExamples.com")
   .getOrCreate()

import spark.implicits._
val columns = Seq("language","users_count")
val data = Seq(("Java", "20000"), ("Python", "100000"), ("Scala", "3000"))
