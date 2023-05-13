function myInfo(a, b) {
    let c
    a = a + b
    b = a + 1
    c = a + b
    return c
}

function info(){}
console.log(info())
console.log(myInfo(1, 3))

const accountPerson = {
    name: "Person one",
    age: 1
}

function upAgePerson(person){
    result = person.age += 1
    return "Результат " + result
}

console.log(accountPerson.age)
console.log(upAgePerson(accountPerson))
console.log(accountPerson.age)
