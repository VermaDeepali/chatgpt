const methods = {};
const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({
  apiKey: process.env.API_KEY,
});
console.log("config", configuration)
const openai = new OpenAIApi(configuration);
methods.getAnswer = (req) => {
    return new Promise(async(resolve, reject) => {
       try{
        console.log("APIKEY", typeof(process.env.API_KEY))
        openai.createCompletion({
            model: "text-davinci-003", // 003 return more detail explanation of the asked question
            prompt: req.body.question,
            "max_tokens": 400, // maximum test return
          }).then((data)=>{
            console.log(data.data.choices,"data")
            // let result = data.data.choices[0].text;
            // result = result.replace(/[\r\n\t]/g, "");
            // console.log(result, "result***")
            // change res from json to text
            resolve({status:200,message: data.data.choices[0].text});

          });

       }catch(e){
          reject(e);
       }
    })
}
module.exports = methods;