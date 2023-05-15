// const strainDetail = {
//    id: 1,
//    category: "category",
//    actual: true
//}

//const newStrainDetail = Object.assign({}, strainDetail)

// newStrainDetail.id = 2
//const name = "name"
//console.log(name)
//console.log(strainDetail)
//console.log(newStrainDetail)

//function myInfo(a, b) {
//    let c
//    a = a + b
//    b = a + 1
//    c = a + b
//    return c
//}

//function info(){}
//console.log(info())
//console.log(myInfo(1, 3))

//const accountPerson = {
//    nameis: "Person one",
//    age: 1
//}

//function upAgePerson(person){
//    result = person.age += 1
//    return "Результат " + result
//}

//console.log(accountPerson.age)
//console.log(upAgePerson(accountPerson))
//console.log(accountPerson.age)

const account = {
    myName: "Test",
    city: ""
}
// const myName = "Igor";
// const city = "Budva";

function returnNameAddress(name, address){
    const updateUser = Object.assign(account, {})
    let nameUser = name;
    let cityUser = address;
    updateUser.myName = nameUser;
    updateUser.city = cityUser;
    console.log(`First User ${account.myName}`)
    console.log(`My Name ${updateUser.myName} i'm from ${updateUser.city}`)
}

returnNameAddress("Igor", "Budva")

const myFunction = function (a, b){
    return c = a + b;
}

console.log(myFunction(1, 2))

const strainPost = {
    id: 1
}
const newCategoryArray = new Array("Indica", "Sativa", "Hybrid");
const strainNamePost = "Strain Name";

const newStrain = (strain, strainName, category, data = Date()) => ({
...strain,
strainName,
category,
data
})

const strainDetail = newStrain(strainPost, strainNamePost, newCategoryArray[1])
if (!strainDetail.id) {
    console.log(`strain detail === 0: ${strainDetail.id}`)
}
else {
    console.log(strainDetail)
}
