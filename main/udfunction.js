function schema_function(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.Location = values[0];
    obj.Temprature = values[1];
    obj.feels_like = values[2];
    obj.humidity = values[3];
    obj.visibility = values[4];
    obj.Wind_speed = values[5];
    obj.pressure = values[6];
    obj.date = values[7];
    obj.time = values[8];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }