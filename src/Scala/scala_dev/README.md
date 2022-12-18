<h1 align="center"><b> Scala 3 SBT Project </b></h1>

<br/>

Just a project space I'm using while I learn Scala.

## **Notes**

To create a new Scala 3 Project from the terminal :

````cli
cd <PROJECT FOLDER>
sbt new scala/scala3.g8
````

Once the project is ready to run, with admin rights : 

````cli
cd <PROJECT FOLDER>
sbt
~run
````

Now the code is running in the terminal and will updated as the code is saved. To run without update on save, ommit '~' from the run statement.

This is a normal sbt project : 

- You can compile code with `sbt compile`
- Run it with `sbt run`
- Start a Scala3 REPL with `sbt console`

**REF**

For more information on the sbt-dotty plugin, see the
[scala3-example-project](https://github.com/scala/scala3-example-project/blob/main/README.md).
