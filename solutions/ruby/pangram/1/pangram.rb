=begin
Write your code for the 'Pangram' exercise in this file. Make the tests in
`pangram_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/pangram` directory.
=end

class Pangram
    ALPHABET = [*"a".."z"].freeze
    def self.pangram?(sentence)
        for letter in ALPHABET
            return false unless sentence.downcase.include?(letter)
        end
        true
    end
end