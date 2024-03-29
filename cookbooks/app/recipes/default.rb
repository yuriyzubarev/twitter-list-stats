#
# Cookbook Name:: git
# Recipe:: default
#
# Copyright 2008-2009, Opscode, Inc.
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

easy_install_package "nose" do
  action :install
end

easy_install_package "nosegae" do
  action :install
end

package "unzip" do
    action :install
end

remote_file "/tmp/gae.zip" do
  source "http://googleappengine.googlecode.com/files/google_appengine_1.5.3.zip"
end

execute "unzip" do
  cwd "/usr/local"
  command "unzip /tmp/gae.zip"
  action :run
end
