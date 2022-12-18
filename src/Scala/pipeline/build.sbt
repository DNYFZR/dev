val scala3Version = "3.2.0"

lazy val root = project
  .in(file("."))
  .settings(
    name := "pipeline",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    libraryDependencies += "org.apache.spark" %% "spark-sql" % "3.0.0-preview2" %% "org.scalameta" %% "munit" % "0.7.29" % Test 
  )
