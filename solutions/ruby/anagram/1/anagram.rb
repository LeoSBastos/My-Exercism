=begin
Write your code for the 'Anagram' exercise in this file. Make the tests in
`anagram_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/anagram` directory.
=end

class Anagram
  def initialize(word)
    @word = word.downcase
  end

  def match(candidates)
    wordList = @word.chars.sort
    anagrams = Array.new
    for candidate in candidates
      if candidate.length != @word.length || candidate.downcase == @word.downcase
        next
      end
      candidateList = candidate.downcase.chars.sort
      if wordList.eql?(candidateList)
        anagrams.push(candidate)
      end
    end
    anagrams
  end
end
