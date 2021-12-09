# pkwu-lab-5

# Routes

You'll find here the routes exposed by this repository. Note that you can also review them through the interactive API docs. The interactive API docs are located at `/docs` and `/redoc`

## Companies router

<br>

### **Search companies**

#### GET `/search`

#### **Query Params**

| Type     | Name | Optional | Description                            |
| -------- | ---- | -------- | -------------------------------------- |
| `string` | `q`  | No       | name of the desired company or service |

#### **Description**:

Web scraper for https://panoramafirm.pl/. Creates VCards from search results.

#### **Sample Requests**

1. http://localhost:8081/search?q=hydraulik
2. http://localhost:8081/search?q=weterynarz
3. http://localhost:8081/search?q=komornik
4. http://localhost:8081/search?q=manufaktura
