class Mycliapp < Formula
  include Language::Python::Virtualenv

  desc "MyCliApp"
  homepage "https://github.com/sullrich84/homebrew-mycliapp"
  head "https://github.com/sullrich84/homebrew-mycliapp.git",
    :branch => "main"

  depends_on "python@3.9"

  resource "argparse" do
    url "https://files.pythonhosted.org/packages/18/dd/e617cfc3f6210ae183374cd9f6a26b20514bbb5a792af97949c5aacddf0f/argparse-1.4.0.tar.gz"
    sha256 "62b089a55be1d8949cd2bc7e0df0bddb9e028faefc8c32038cc84862aefdd6e4"
  end

  def install
    virtualenv_install_with_resources
  end

  # test do
  #   assert_match "sullrich84/atlas 0.0.0-alpha", shell_output("#{bin}/atlas")
  # end
end
