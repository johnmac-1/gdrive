from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1568165692:AAEXDAppAjX7-7d0p4nph6oe2GGl2bh4_SI"
    APP_ID = 2094034
    API_HASH = "6d15ffa47d372a191aa8fcf9e4d175e6"
    OWNER_ID = 1284331504
    AUTH_CHANNEL = [-1001481042970]
    DESTINATION_FOLDER = "Gdrivebot" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG ="""
[DRIVE]
type = drive
scope = drive
token = {"access_token":"ya29.a0AfH6SMB9Jsx__bNmnUM5VDoxKbQCjYaZBTWIaTEsMEaU_F0SEtEoSpMelF2lVviafkIrzjAuorJfRDwbIwlpPM9XgcM3hl3S_jnHUkNf-GB9T2VY8Zmld33PtnCt4nXrS5FQ1v_4x0WywdFZcsCzzMEHXSDgB5InqRdvsQ84l78","token_type":"Bearer","refresh_token":"1//0g1etf7uezWRbCgYIARAAGBASNwF-L9IrQIg78Ecrkdo4njd8RzINecmBWAGwRujihPFbZrISgIRXXMHw62jtEgSI1GyW-e8LdnA","expiry":"2021-01-23T07:21:01.502901964Z"}
team_drive = 0ABC30BE8KaZeUk9PVA
"""
