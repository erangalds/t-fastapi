# MongoDB Primer

## Step 1: Connect to MongoDB

First I wanted to connect to MongoDB instance. 

+ Connect to the *mongo_db* container instance using shell

    ```bash
    docker container exec --interactive --tty mongo_db mongosh
    ```

    I got a some messages and the `>` prompt, which means I have successfully connected to the mongodb instance.

## Step 2: Database in MongoDB

I found out that MongoDB organizes data into databases. A single MongoDB instance can host multiple databases. Now let's try to see how to list the current databases using `mongoshell`

```javascript
show dbs
```

Write, thata worked. I can see that there are 4 databases currently in my mongodb instance. The current databases are admin, config, local, and mydemodb. I later found out that admin, config and local are internal databases of mongodb. 

Now let me try to connect to one of the databases, and try to see what's inside. I can use the `use` command to connect to an existing *database*. 

```javascript
use mydemodb
```

I got a message saying, the db switched to `mydemodb`, which means that I am now connected to the `mydemodb` database. 

Let me try to list my current database to confirm again. 

```javascript
db
```

I see the output as `mydemodb`, which confirms that I am connected to the `mydemodb` database. 

## Step 3: Collections in MongoDB

What I learnt is that data organization hierarchy in mongodb is database > collection > documents.

Going a little bit detail to clarify the distiction of the three. 

+ **Databases**: The top-level logical container for your data. Each databases representing a different application or logical data separation. 
+ **Collections**: Collections holds groups of documents. They are analogous to tables in a relational database. The collections are "schemaless" or "schema-flexible". Putting that into simple words, is that, the documents within the same collection don't need to have identical structures. 
+ **Documents**: Fundamental unit of data in mongodb. Documents are `BSON (Brinary JSON)` objects, which are essentially key-value pairs, similar to JSON. Each document has a unique `_id` field. 

The next question which came to my mind was, "what are indexes in mongodb?". Well what I found was, indexes are not a layer of data organization in the same way as databases and collections. Instead, indexes are data structures that mongodb maintains on collections to speed up queries for retrieval.

So, then let's try to see whether there are any `collections` in the `mydemodb`

```javascript
show collections
```

I can see `mycollection` as the output, which confirms that there is only one collection in the `mydemodb` database currently. 

Now I want to see what's inside the `mycollection`. Let me try to read the collection and see what's inside. I found out that I can do that with the `db.mycollection.find()` function. Let me try to do that now. 

Since I want to see everything under `mycollection`, I can leave the filter empty. 

```javascript
db.mycollection.find() 
```

## Step 4: Create a new Database and Collection and Insert Documents

### Create a new Database

What I found was that using the `use` command I can create a new database. What actually happens is that mongodb will check whether the given database exists, if yes, then connects me to the database, otherwise it will create this new database. 

Let me now try to create a new database named `fastapi_training_db`

```javascript
// creating a new database
use fastapi_training_db
// confirming the current database
db
// output: fastapi_training_db
// listing the current collections
show collections
// output: []
```

### Create a new Collection

Similar to the databases, collections can be created implicitly, which means it gets created automatically, when we start to insert our first document. 

#### Insert a single document
Let me try to create a new collection named `courses` by inserting a document into it. Looks like I can do that with the `db.<collection_name>.insertOne()` function. So for this requirement it will be `db.courses.insertOne()` function. 


```javascript
db.courses.insertOne({
    "title": "Introduction to FastAPI",
    "description": "Learn the basics of building APIs with FastAPI",
    "duration_hours": 8,
    "topics": ["Basics","Routing","Path Parameters","Query Parameters"],
    "level": "Beginner",
    "is_published": true
})

// output: {"acknowledged": true, "insertedId: ObjectId('6850c74bf51d106dbc1b5ff2')"}
```

### Insert multiple documents

Most of the time, we might have to insert multiple documents into a collection. I found out that `insertMany()` can help us to do that. Let me try to do 

```javascript
db.courses.insertMany([
    {
        "title": "FastAPI Authentication and Authorization",
        "description": "Secure your FastAPI applications with authentication and authorization.",
        "duration_hours": 12,
        "topics": ["OAuth2", "JWT", "Permissions"],
        "level": "Intermediate",
        "is_published": false
    },
    {
        "title": "Advanced FastAPI: Databases and Deployment",
        "description": "Connect FastAPI to databases and deploy your applications.",
        "duration_hours": 16,
        "topics": ["SQLAlchemy", "MongoDB", "Docker", "Deployment"],
        "level": "Advanced",
        "is_published": true
    },
    {
        "title": "FastAPI Testing and Best Practices",
        "description": "Learn how to test your FastAPI apps and follow best practices.",
        "duration_hours": 20,
        "topics": ["Pytest", "Testing strategies", "Dependency Injection"],
        "level": "Intermediate",
        "is_published": true 
    }
])
```

I received an array of `insertedIds`. 

## Step 5: Read Documents

Now I have creatd my own small database and a collection inside with couple of documents. Let me now try to see the ways in which I can retrieve them. 

What I found is that `find()` is what comes to help. 

**Retrieving all documents**
This is equal to a SELECT * FROM <TABLE_NAME> in SQL. What I found is that I need to use `find()` without specifying any filtering criteria. 

```javascript
db.courses.find()
```
Earlier I had inserted 4 documents, and I got all 4 documents back. 

**Retrieving specific documents**

+ Single Filter
Now I need to know, how to retrieve specific documents, which match specific criteria (filters). Basically the equivalent of a SELECT <COLUMNS> FROM <TABLE_NAME> WHERE clause in SQL.

Let's say I want to find all the course names which where the `level` is `Beginner`. 

```javascript
db.courses.find({
    "level": "Beginner"
})
```
There was only one such course and I got the details back. 

+ Multiple Filters (AND Logic)
Let's say I want courses both level = intermediate and is_published = true. 

```javascript
db.courses.find({
    "level": "Intermediate",
    "is_published": true
})
```
**Query Operators**
MongoDB uses `$` to denote query operators. 
+ greater than: `$gt`
+ less than: `$lt`
+ greater than or equal to: `$gte`
+ less than or equal to: `$lte`
+ not equal to: `$ne`
+ in: `$in` (values in an array)
+ not in: `$nin` (values in an array)
+ regular expressions for text search: `$regex`


**Using query operators**

```javascript
//Courses with a duration greater than 10 hours
db.courses.find({
    "duration_hours": {
        "$gt": 10
    }
})

//Courses with a duration less than 10 hours
db.courses.find({
    "duration_hours": {
        "$lt": 10
    }
})

//Courses with a duration greater than 10 and less than  14 hours 
db.courses.find({
    "duration_hours": {
        "$gt": 10,
        "$lt": 18
    }
})

//Courses where level is either Beginner or Intermediate
db.courses.find({
    "level": {
        "$in": ["Beginner", "Intermediate"]
    }
})

//Courses where level is not Beginner or Intermediate
db.courses.find({
    "level": {
        "$nin": ["Beginner", "Intermediate"]
    }
})

//Courses where level is not Beginner
db.courses.find({
    "level": {
        "$ne": "Beginner"
    }
})

//Courses where Title has FastAPI in it
db.courses.find({
    "title": {
        "$regex": /FastAPI/
    }
})

db.courses.find({
    "title": {
        "$regex": /FastAPI/,
        "$options": "i" // case insensitive
    }
})
    
```

**Selecting different fields**
In our SELECT statement in SQL we can select which columns should be included in our results set. We can do that by specifying the required column names in the SELECT query. I wanted to check whether we can do the same in MonboDB (we should be able to). Specifying the column with either 1 or 0 does the trick where 1 means to include and 0 is to exclude from the results. 

```javascript
//Let's say I want courses course title and duration, without _id column. _id is 1 by default. 
db.courses.find({}, {
    "title": 1,
    "duration_hours": 1,
    "_id": 0
})
```

**Chaining Modifiers ( .pretty(), .sort(), .limit(), .count() )**

```javascript
// .pretty
db.courses.find().pretty()

// .sort
db.courses.find().sort({
    "duration_hours": 1 // ascending order
})

db.courses.find().sort({
    "duration_hours": -1 // descending order    
})

// .limit
db.courses.find().limit(2) // Get only 2 documents

// .count
db.courses.find().count()

// .count with filters
db.courses.find({
    "level": "Beginner"
}).count()
```

## Step 6: Update Documents

Next important I need to learn is how to update the inserted documents. Looks like `updateOne()` and `updateMany()` methods can be used to modify the existing documents. 

**Updating a single document**

What I found is that we need to use two arguments. First argument is the query to find or locate the document(s) to be modified. The second is the update operator. We need to use $set to se a field and $inc to increment a field etc. 

```javascript
//changing the is_published and adding a new field
db.courses.updateOne(
    {
        "title": "FastAPI Authentication and Authorization"
    },
    {
        $set: {
            "is_published": true,
            "updated_at": new Date()
        },     
    },
)
```
I got an update saying acknowledged: true, matchedCount: 1 and modifiedCount: 1. 

Let me verify this again by a `.find()`

```javascript
db.courses.find({
    "title": "FastAPI Authentication and Authorization"
})
```
I can see that the `is_published` is now `true`. The new `updated_at` field is added with the timestamp. 

**Updating multiple documents**

I am going to use `.updateMany()` for this. 

```javascript
//Adding another topic to topic list with $push 
db.courses.updateMany(
    {
        "level": "Beginner"
    },
    {
        $push: {
            "topics": "core_concepts"
        }//push adds another element to the array
    }
)
//Let's validate
db.courses.find({
    "level": "Beginner"
})

```
I can see the new topic was added to the topics array. 

## Step 7: Delete Documents
Similar to the insert, update, looks like we have two functions `deleteOne()` and `deleteMany()` to delete documents. 

**Deleting a single document**

```javascript
db.courses.deleteOne({
    "title": "FastAPI Authentication and Authorization"
})
```
**Deleting multiple documents**

```javascript
db.courses.deleteMany({
    "level": "Intermediate"
})
```

## Step 8: Dropping a Collection or a Databases

**Dropping Collections**
`.drop()` is the function to use. 

Let me try to delete the `courses` collection now. 

```javascript
db.courses.drop()
```

***Drop Database**

`.dropDatabase()` is the function to use. 

```javascript
db.dropDatabase()
```

Great. What a day. It was fun to learn the main topics about this very famouse and widely used database. 




