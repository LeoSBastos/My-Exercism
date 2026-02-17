=begin
Write your code for the 'Space Age' exercise in this file. Make the tests in
`space_age_test.rb` pass.

To get started with TDD, see the `README.md` file in your
`ruby/space-age` directory.
=end

class SpaceAge
    def initialize(seconds)
        @years = seconds/31557600.to_f
    end
    def on_earth
        @years
    end
    def on_mercury
        @years/0.2408467
    end
    def on_venus
        @years/0.61519726
    end
    def on_mars
        @years/1.8808158
    end
    def on_jupiter
        @years/11.862615
    end
    def on_saturn
        @years/29.447498
    end
    def on_uranus
        @years/84.016846
    end
    def on_neptune
        @years/164.79132
    end
end