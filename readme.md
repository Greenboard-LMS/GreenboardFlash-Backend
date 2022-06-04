# Greenboard API 
> **Info**: There will be a header for passing the authorization token when making authenticated requests 

---
### Cardsets
#### Get List of Cardsets
```javascript
// api.greenboard.com/flash/cardsets/
// method: GET
```
```javascript
[
	{
		id: 1,
		owner: {
			id: 1, 
			username 'greenboard.user'
		},
		title: 'Cardset Title',
		flashcard_count: 10, 
	}, 
	{
		id: 2,
		owner: {
			id: 1, 
			username 'greenboard.user'
		},
		title: 'Cardset Title 2',
		flashcard_count: 5, 
	}
]
```

#### Get a Cardset with a specific id
```javascript
// api.greenboard.com/flash/cardsets/1/
// method: GET
```
```
{
	id: 1,
	owner: {
		id: 1, 
		username 'greenboard.user'
	},
	title: 'Cardset Title',
	flashcard_count: 10, 
}
```

#### Creating a Cardset
```javascript
// api.greenboard.com/flash/cardsets/
// method: POST
```
```
// Expected structure of request body
{
	title: 'Cardset Title',
}

// Response body (if successful)
{
	id: 1,
	owner: {
		id: 1, 
		username 'greenboard.user'
	},
	title: 'Cardset Title',
	flashcard_count: 10, 
}
```

#### Updating a Cardset
```javascript
// api.greenboard.com/flash/cardsets/1/update/
// method: POST
```
```
// Expected structure of request body
{
	title: 'Cardset Title (updated)',
}

// Response body (if successful)
{
	id: 1,
	owner: {
		id: 1, 
		username 'greenboard.user'
	},
	title: 'Cardset Title (updated)',
	flashcard_count: 10, 
}
```
---
### Flashcards
#### Get a List of Flashcards from a specific Cardset
```javascript
// api.greenboard.com/flash/cardsets/1/cards
// method: GET
```
```
[
	{
		id: 1,
		question: 'How high is Mount Everest?',
		answer: '8848m',
		cardset: 1,
	}, 
	{
		id: 2,
		question: 'Is this a good question?',
		answer: 'Yes',
		cardset: 1,
		
	},
	{
		id: 3,
		question: 'Is Greenboard amazing?',
		answer: 'YES!',
		cardset: 1,
	}
]
```

#### Get a specific Flashcard from a specific Cardset
```javascript
// api.greenboard.com/flash/cardsets/1/cards/1
// method: GET
```
```
{
	id: 1,
	question: 'How high is Mount Everest?',
	answer: '8848m',
	cardset: 1,
}
```

#### Create a Flashcard inside a specific Cardset
```javascript
// api.greenboard.com/flash/cardsets/1/cards/
// method: POST
```
```
// Expected structure of request body
{
	question: 'Is this my first self-made question?',
	answer: 'yes!',
}

// Response body (if successful)
{
	id: 1, 
	question: 'Is this my first self-made question?',
	answer: 'yes!',
	cardset: 1,
}
```

#### Update a specific Flashcard inside a specific Cardset
```javascript
// api.greenboard.com/flash/cardsets/1/cards/1/update/
// method: POST
```
```
// Expected structure of request body (no field will probably be required, so you could just send the question over for example)
{
	question: 'Is this my first self-made question (updated)?',
}

// Response body (if successful)
{
	id: 1, 
	question: 'Is this my first self-made question? (updated)',
	answer: 'yes!',
	cardset: 1,
}
```

--- 

### Users/Authentication
#### Generating/Receiving a Token for User Credentials
```javascript
// api.greenboard.com/users/token/
// method: POST
```
```json
// Expected request body:
{
	username: 'USERNAME',
	password: 'PASSWORD' 
}, 

// Response (if successful): 
{
    token: "123456789abcdefgh"
}
```

#### Making authenticated Requests
```javascript
// You always need to add this header to requests:
{
	Authorization: "Token <TOKEN>"
}, 
```