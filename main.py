#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from functions import valid_email
from functions import valid_user
from functions import valid_password
from functions import sub
import webapp2
import cgi
from functions import escape

form = """
<form method="post">
    <fieldset>
        <legend>Signup</legend>
        <label>Username
        <input type = "text" name="username" value="%(username)s"/>
        <font style="color: red">%(error_user)s</font>
        </label>
        <br>
        <label>Password
            <input type="password" name="password"/>
            <font style="color: red">%(error_password)s</font>
        </label>
        <br>
        <label>Re-enter Password
            <input type="password" name="repassword"/>
            <font style="color: red">%(error_match)s</font>
        </label>
        <br>
        <label>Email (optional)
            <input type="text" name="email" value="%(email)s"/>
            <font style="color: red">%(error_email)s</font>
        </label>
        <br>
        <input type="Submit"/>
    </fieldset>
</form>
"""
class MainHandler(webapp2.RequestHandler):
    def write_form(self, error_user="", error_email="", error_match="",
    error_password="", username="", email=""):
        self.response.out.write(form % {"error_user":error_user,
                                        "error_email":error_email,
                                        "error_match":error_match,
                                        "error_password":error_password,
                                        "username":escape(username),
                                        "email":escape(email)})
    def get(self):
        self.write_form()

    def post(self):
        ded_username = self.request.get("username")
        ded_password = self.request.get("password")
        ded_repassword = self.request.get("repassword")
        ded_email = self.request.get("email")

        username = valid_user(ded_username)
        email = valid_email(ded_email)
        match = ""
        password = valid_password(ded_password)
        if ded_password == ded_repassword:
            match = ded_password
        error_user = ""
        error_email = ""
        error_match = ""
        error_password = ""

        if not (username):
            error_user = "Please enter a username with no spaces"
        if not (email):
            error_email = "Email must contain an @ and .com"
        if match != ded_password:
            error_match = "Passwords do not match"
        if ded_password == "":
            error_password = "Invalid Password"
        self.write_form(error_user, error_email, error_match, error_password,
         ded_username, ded_email)

        if (username and email and match and password):
            self.redirect("endpage")

class EndHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.out.write(sub(username))

app = webapp2.WSGIApplication([
    ('/', MainHandler),("/endpage",EndHandler)
], debug=True)
