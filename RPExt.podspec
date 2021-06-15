#
# Be sure to run `pod lib lint RPExt.podspec' to ensure this is a
# valid spec before submitting.
#
# Any lines starting with a # are optional, but their use is encouraged
# To learn more about a Podspec see https://guides.cocoapods.org/syntax/podspec.html
#

Pod::Spec.new do |s|
  s.name             = 'RPExt'
  s.version          = '0.1.0'
  s.summary          = 'RPExt using to learn podspec.'

# This description is used to generate tags and improve search results.
#   * Think: What does it do? Why did you write it? What is the focus?
#   * Try to keep it short, snappy and to the point.
#   * Write the description between the DESC delimiters below.
#   * Finally, don't worry about the indent, CocoaPods strips it!

  s.description      = <<-DESC
Using to learn podspec creation jsdf sjds sjdfsdj djvfdsjf sdjfsdhf jsdf jh.
                       DESC

  s.homepage         = 'https://github.com/RenukaPa/RPExt'
  # s.screenshots     = 'www.example.com/screenshots_1', 'www.example.com/screenshots_2'
  s.license          = { :type => 'MIT', :file => 'LICENSE' }
  s.author           = { 'Renuka Pandey' => 'renukapandey90@gmail.com' }
  s.source           = { :git => 'https://github.com/RenukaPa/RPExt.git', :tag => s.version.to_s }
  # s.social_media_url = 'https://twitter.com/<TWITTER_USERNAME>'

  s.ios.deployment_target = '9.0'

  s.source_files = 'RPExt/Classes/**/*'
  
  # s.resource_bundles = {
  #   'RPExt' => ['RPExt/Assets/*.png']
  # }

  # s.public_header_files = 'Pod/Classes/**/*.h'
   s.frameworks = 'UIKit'
#   , 'MapKit'
  # s.dependency 'AFNetworking', '~> 2.3'
end
