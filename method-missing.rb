# Using method_missing to handle dynamic method calls
class DynamicHandler
    def method_missing(name, *args)
        if name.to_s.start_with?('handle_')
            # Custom handling logic
            puts "Handling #{name}"
        else
            super
        end
    end
end
