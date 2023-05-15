const profile = {
    name: "",
    nick: "",
    age: 0
}

const changeProfile = (name, nick, age) => ({
    name,
    nick,
    age
})

const testName = "Name";
const testNick = "Nick";
const testAge = 12;


const profileAge = changeProfile(testName, testNick, testAge)
if (profileAge.age >= 18){
    console.log(`Access you age: ${profileAge.age}`)
}
else {
    console.log(`Min Age 18 you age:  ${profileAge.age}`)
}


/// console.log(changeProfile(testName, testNick, testAge))