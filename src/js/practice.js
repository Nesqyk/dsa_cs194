// Excercise 1 

// This function works, but it's "old"
function getProfileString(user) {
  var firstName = user.firstName;
  var lastName = user.lastName;
  var profession = user.profession;

  var str = "Name: " + firstName + " " + lastName + ", Profession: " + profession;
  return str;
}

// How we'd use it:
var user = {
  firstName: "Jane",
  lastName: "Doe",
  profession: "Developer"
}

console.log(getProfileString(user));

// Update and Answer
const get_profile = (user) => `Name: ${user.firstName} ${user.lastName}, Profession: ${user.profession}`;

console.log(get_profile(user))

// --

// Exercise 2:  The Data Fetcher (async/await)

// A fake function to simulate fetching data
function mockFetch(isSuccess) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (isSuccess) {
        resolve({ id: 1, name: "John Doe" });
      } else {
        reject(new Error("Failed to fetch data"));
      }
    }, 1000); // 1-second delay
  });
}

let fetch_user = async () => {
    console.log("Fetching user...");
    try {
        const data = await mockFetch(true);
        console.log("Success:", data)
    } catch (error) {
        console.error("Error: ", error.message)
    }    
}

fetch_user()


// Exercise 3:

const products = [
  { id: 1, name: "Laptop", category: "Electronics", price: 1200, stock: 8 },
  { id: 2, name: "Coffee Maker", category: "Appliances", price: 80, stock: 15 },
  { id: 3, name: "Headphones", category: "Electronics", price: 150, stock: 0 },
  { id: 4, name: "Blender", category: "Appliances", price: 60, stock: 12 },
  { id: 5, name: "Keyboard", category: "Electronics", price: 90, stock: 20 }
];


// Challenge 3.1: Get In-Stock Electronics (.filter())
const inStockElectronics = products.filter(products => products.stock > 0 && products.name === "Electronics");

// Challenge 3.2: Get Product Names (.map())
const productNames = products.map(products => products.name)

console.log(inStockElectronics, productNames)


